from transformers import BertForTokenClassification, BertTokenizer
import nltk
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
from keras.preprocessing.sequence import pad_sequences

tag2idx = {'I-per': 0,
           'B-eve': 1,
           'B-nat': 2,
           'I-eve': 3,
           'I-art': 4,
           '[CLS]': 5,
           'I-nat': 6,
           'B-gpe': 7,
           '[SEP]': 8,
           'O': 9,
           'I-org': 10,
           'I-geo': 11,
           'B-per': 12,
           'B-org': 13,
           'I-gpe': 14,
           'I-tim': 15,
           'B-art': 16,
           'B-tim': 17,
           'B-geo': 18,
           'X': 19}

max_len = 45
bert_out_address = 'model/bert_out_model'

bert_model = BertForTokenClassification.from_pretrained(bert_out_address, num_labels=len(tag2idx))
tokenizer = BertTokenizer.from_pretrained(bert_out_address)

def bert_preprocess(text):
    word_tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(word_tokens)
    tokenized_texts = []
    temp_token = []
    temp_token.append('[CLS]')

    for word, lab in pos_tags:
        token_list = tokenizer.tokenize(word)
        for m, token in enumerate(token_list):
            temp_token.append(token)
    
    temp_token.append('[SEP]')
    tokenized_texts.append(temp_token)
    input_ids = pad_sequences([tokenizer.convert_tokens_to_ids(txt) for txt in tokenized_texts], maxlen=max_len, dtype='long', truncating='post', padding='post')
    return input_ids, word_tokens

def extract_features(word, i, new_sentence):
    """Extract features from a sentence for CRF prediction."""
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit()
    }

    if i > 0:
        word1 = new_sentence[i - 1]  # Access previous word from new_sentence
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper()
        })
    else:
        features['BOS'] = True

    if i < len(new_sentence) - 1:
        word1 = new_sentence[i + 1]  # Access next word from new_sentence
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper()
        })
    else:
        features['EOS'] = True

    return features

def crfs_preprocess(text):
    new_sentence = text.split()

    X_test = [extract_features(word, i, new_sentence) for i, word in enumerate(new_sentence)]
    X_test = [X_test]
    return X_test, new_sentence