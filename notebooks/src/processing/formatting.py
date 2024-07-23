import os
import glob
import cv2 as cv
import numpy as np
from sklearn import preprocessing
from sklearn.utils import shuffle
import pickle
def formatting(filepath):
    
    images = []
    labels = []
    
    for directory_path in glob.glob(filepath):
        label = directory_path.split("\\")[-1]
        print(label)
        for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
            print(img_path)
            img = cv.imread(img_path, cv.IMREAD_COLOR)
            img = cv.resize(img, (256,256))
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            images.append(img)
            labels.append(label)

    images = np.array(images)
    labels = np.array(labels)
    
    le = preprocessing.LabelEncoder()
    le.fit(labels)
    labels = le.transform(labels)
    
    os.chdir(r'C:\Users\randy\OneDrive\Desktop\CS\curvedanomalydetection')
    output = open('encoder.pkl', 'wb')
    pickle.dump(le, output)
    output.close()

    images = images / 255.0
    
    images, labels = shuffle(images, labels)
    return images, labels
    
    


    