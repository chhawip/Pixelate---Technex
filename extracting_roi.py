import numpy as np
import cv2

img = cv2.imread('friends.png', cv2.IMREAD_COLOR)

px=img[55,55]      #this gives the color values of px
img[55,55]=[255,255,255]     #assigning pixel color


#region of image (roi)
roi = img[100:150 , 100:150]
print(roi)      #print all pixel values lying in that range

part=img[150:200 , 150:250]      #taking a part of img and storing it in part
img[0:50 , 0:100]=part           #assigning top left corner of image to part

cv2.imshow('friends', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

add=img1+img2    #here pixels don't loose their opaqueness
cv2.add(img1,img2)    #here [155,211,79] + [50,170,200] + ..... = [205,381,279] translated to [205,255,255] hence, mostly bright

#weighted addition
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)

