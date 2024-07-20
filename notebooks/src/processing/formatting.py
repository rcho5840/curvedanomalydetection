import glob
import cv2 as cv
import numpy as np
from sklearn import preprocessing
    
def formatting(filepath):
    
    # Create empty lists and set the pixel size of the images
    images = []
    labels = []
    SIZE = 256
    
    # traverse through the anomaly and normal folders while traversing through the indvidiual design types 
    # Set labels according to the names of the files. For example "da" refers to diskanomaly
    # Findally, traverse through the images within each design folder and convert to grayscale, resize, and append to the list
    for directory_path in glob.glob(filepath + '\*'):
        if directory_path == "Anomaly":
            label = "anomaly"
        else:
            label = "normal"
        for img_path in glob.glob(directory_path + "\*"):
            if img_path.endswith(".jpg"):  
                print(img_path)
                img = cv.imread(img_path, cv.IMREAD_COLOR)
                img = cv.resize(img, (SIZE, SIZE))
                img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
                images.append(img)
                labels.append(label)
    
    #Convert lists to numpy arrays and use one hot encoding to make labels numerical
    images = np.array(images)
    labels = np.array(labels)
    encoder = preprocessing.LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)
    
    #Normalize the pixel values and return the image set and label set. You will do this for both the training data and testing data
    images = images / 255.0
    return images, encoded_labels

    