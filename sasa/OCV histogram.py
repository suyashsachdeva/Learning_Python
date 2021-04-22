import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt

link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
#cv.imshow('image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gary', gray)

circle = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, thickness= -1)
masked = cv.bitwise_and(gray,gray, mask=circle)
cv.imshow('masked image', masked)

#1. Grayscale histogram
grayh = cv.calcHist([masked], [0], None, [256], [0,256])
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixel')
plt.plot(grayh)
plt.xlim([0, 256])



#2. Color Histogram
colors =('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i],circle, [256], [0,256])
    plt.plot(hist, color= col)

plt.show()
cv.waitKey(0)