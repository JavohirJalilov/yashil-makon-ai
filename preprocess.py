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

    image = cv2.GaussianBlur(image,(5,5),0)
    imgHSV = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    img1 = copy.deepcopy(image)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel(5,5))
    closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel(3,3))


    contours,heirarchy = cv2.findContours(closing,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
    # img1 = cv2.drawContours(img1,contours,-1,(255,0,0),thickness=-1)
    k=0
    parents_not_child=[]
    for i in heirarchy[0]:

        if i[-2]==-1:
            parents_not_child.append(k)
        k+=1

    for i,pnt in enumerate(parents_not_child):
        cnt = contours[i]
        
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt,True)
        x,y,w,h = cv2.boundingRect(cnt)
        img1 = cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
    
    H, W, CH = img1.shape
    split_image = np.full((H, 10,CH), 255, dtype=np.uint8)

    result_image = np.hstack((image, split_image, img1))
    return result_image