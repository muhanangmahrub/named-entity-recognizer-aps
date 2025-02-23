from inference.preprocess import crfs_preprocess, bert_preprocess, bert_model
import joblib
import torch
import torch.nn.functional as F

models = ['spacy', 'crfs', 'bert']
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tag2name = {0: 'I-per', 
            1: 'B-eve',
            2: 'B-nat',
            3: 'I-eve',
            4: 'I-art',
            5: '[CLS]',
            6: 'I-nat',
            7: 'B-gpe',
            8: '[SEP]',
            9: 'O',
            10: 'I-org',
            11: 'I-geo',
            12: 'B-per',
            13: 'B-org',
            14: 'I-gpe',
            15: 'I-tim',
            16: 'B-art',
            17: 'B-tim',
            18: 'B-geo',
            19: 'X'}

def inference_spacy(text):
    nlp = joblib.load("model/ner_model.joblib")
    doc = nlp(text)
    words = text.split()
    result = {}
    have_label = False
    for word in words:
        for ent in doc.ents:
            if word == ent.text:
                result[word] = ent.label_
                have_label = True
        if not have_label:
            result[word] = '0'
        have_label = False
    return result

def inference_crf(text):
    result = {}
    X_test, new_sentence = crfs_preprocess(text)
    crf = joblib.load('model/crf.joblib')
    y_pred = crf.predict(X_test)
    for word, label in zip(new_sentence, y_pred[0]):
        result[word] = label
    return result

def inference_bert(text):
    result = {}
    input_ids, word_tokens = bert_preprocess(text)
    attention_masks = [[int(i>0) for i in ii] for ii in input_ids]
    input_ids = torch.tensor(input_ids).to(device)
    attention_masks = torch.tensor(attention_masks).to(device)

    with torch.no_grad():
        outputs = bert_model(input_ids, token_type_ids=None,
                    attention_mask=attention_masks)
        logits = outputs[0]
    logits = torch.argmax(F.log_softmax(logits,dim=2),dim=2)
    logits = logits.detach().cpu().numpy()
    predicted_labels = [tag2name[logit] for logit in logits[0]]
    for i in range(len(word_tokens)):
        result[word_tokens[i]] = predicted_labels[i+1]
    return result

def predict_text(model, text):
    if model == models[0]:
        result = inference_spacy(text)
    elif model == models[1]:
        result = inference_crf(text)
    elif model == models[2]:
        result = inference_bert(text)
    return result

result = inference_bert("The Israeli army has killed a Palestinian youth in the northern Gaza Strip and wounded at least three other people")
print(result)
