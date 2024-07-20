import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def flannautocropping(standardpath, targetpath):
    
    standard = cv.imread(standardpath) # standard
    
    target = cv.imread(targetpath) # image that will be cropped
    
    sift = cv.SIFT_create()

    standard_kp, standard_des = sift.detectAndCompute(standard,None)
    target_kp, target_des = sift.detectAndCompute(target,None)
    
    
    
    
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=1000)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    
    matches = flann.knnMatch(standard_des, target_des, k = 2)

    x = []
    y= []
    

    
    for m, n in matches:
        if m.distance < 0.9 * n.distance:
            (x1,y1) = target_kp[m.trainIdx].pt 
            x.append(x1)
            y.append(y1)
    
    x.sort()
    y.sort()

    x_start = int(x[0])
    x_end = int(x[-1])
    y_start = int(y[0])
    y_end = int(y[-1])

    cropped = target[x_start:x_end, y_start:y_end]

    fig = plt.figure(figsize = (10,7))
    fig.add_subplot(2,2,1)
    plt.imshow(standard)
    plt.axis('off')
    plt.title("standard")
    
    fig.add_subplot(2,2,2)
    plt.imshow(target)
    plt.axis('off')
    plt.title("target")
    
    fig.add_subplot(2,2,3)
    plt.imshow(cropped)
    plt.axis('off')
    plt.title("result")
    
    
    
    # bf = cv.BFMatcher(cv.NORM_L1,crossCheck=False)

    # matches = bf.match(standard_des,target_des)
    # find the keypoints and descriptors