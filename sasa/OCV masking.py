import cv2 as cv 
import numpy as np 

link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
cv.imshow('image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


# Masking of a images
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 125, 255, -1)
cv.imshow('mask', mask)
#masked = cv.bitwise_and(img, img, mask=mask)
#cv.imshow('masked image', masked)

mask1 = cv.rectangle(blank, (200,200), (380,380), 255, thickness= -1)
#masked1 = cv.bitwise_and(img, img, mask=mask1)
#cv.imshow('Rectangle mask', masked1)

maskCom = cv.bitwise_and(mask, mask1)
cv.imshow('mask combined', maskCom)
maskedCom = cv.bitwise_and(img, img, mask=maskCom)
cv.imshow('Weird Mask', maskedCom)




cv.waitKey(0)