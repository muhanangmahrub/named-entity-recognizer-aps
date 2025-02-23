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