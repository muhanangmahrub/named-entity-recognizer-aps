from preprocess import crfs_preprocess
import joblib
import json

models = ['SpaCy', 'CRF-Sklearn', 'BERT']

def inference_spacy(text):
    nlp = joblib.load("../model/ner_model.joblib")
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
    return json.dumps(result)

def inference_crf(text):
    result = {}
    X_test, new_sentence = crfs_preprocess(text)
    crf = joblib.load('../model/crf.joblib')
    y_pred = crf.predict(X_test)
    for word, label in zip(new_sentence, y_pred[0]):
        result[word] = label
    return json.dumps(result)


def inference(model, text):
    if model == models[0]:
        result = inference_spacy(text)
    elif model == models[1]:
        result = inference_crf(text)
    return result
        
    
testing = inference('SpaCy', 'Separately , officials say a policeman was killed in Mosul when he tried to move a decapitated body that was rigged with explosives .')
print(testing)