#contour are better at shape recogination 
import cv2 as cv
import numpy as np

link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
cv.imshow('image', img)

blank = np.zeros(img.shape, dtype='uint8')


# Contours vs canny
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)
canny = cv.Canny(blur, 1, 1)
cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

cont, hiera = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(str(len(cont))+" contours where found")
cont1, hiera1 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(str(len(cont1))+" contours where found")

cv.drawContours(blank, cont, -1, (0,0,255), 1)
cv.imshow('draw', blank)





cv.waitKey(0)