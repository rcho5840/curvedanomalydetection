import os
import glob
import cv2
import numpy as np


def formatting(pathway):
    images = []
    labels = []
    SIZE = 256
    for directory_path in glob.glob(pathway):
        label = directory_path.split("\\")
        for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (SIZE, SIZE))
            images.append(img)
            labels.append(label)
    
    images = np.array(images)
    labels = np.array(labels)
    return images, labels