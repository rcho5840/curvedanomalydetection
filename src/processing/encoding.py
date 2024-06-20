from sklearn import preprocessing

def encoding(labels):
    encoder = preprocessing.LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)
    return encoded_labels
    
