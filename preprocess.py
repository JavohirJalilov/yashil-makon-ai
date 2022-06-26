import matplotlib.pyplot as plt
import numpy as np
import cv2
import copy

def kernel(n,m):
    kernel = np.ones((n,m),dtype=np.uint8)
    return kernel

def preprocess(image):
    h_min, h_max = 45, 70
    s_min, s_max = 30, 180
    v_min, v_max = 30, 100

    imgHSV = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    img1 = copy.deepcopy(image)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel(3,3))
    closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel(2,2))

    contours,herarchy = cv2.findContours(closing,cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    # img1 = cv2.drawContours(img1,contours,-1,(255,0,0),thickness=-1)
    
    for cnt in contours:

        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt,True)
        x,y,w,h = cv2.boundingRect(cnt)
        img1 = cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)

    result_image = np.hstack((image,img1))
    return result_image