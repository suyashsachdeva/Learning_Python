import cv2 as cv 

link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


#1. Simple Thersholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)
print(threshold)


#2. Inverse Thersholding
threshold, threshinv = cv.threshold(gray, 50, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', threshinv)


#3. Adaptive Thresholding 
adap = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 15)
cv.imshow('Adaptive Thresholding', adap)
adap_gau = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 15)
cv.imshow('Adaptive Thresholding Gaussian', adap_gau)



cv.waitKey(0)