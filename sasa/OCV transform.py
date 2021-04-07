import cv2 as cv
import numpy as np

link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
cv.imshow('image', img)


#1. Translation function(SHIFT UP, RIGHT, LEFT AND DOWN)
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension =(img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

"""
-x--> Left
-y-->up
x-->right
y-->down
"""

trans= translate(img, -100, 0)
#cv.imshow('Translated', trans)


#2. Roation of Image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width/2,height/2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width,height)

    return cv.warpAffine(img, rotMat, dimension) 
     
rot = rotate(img, 45)
#cv.imshow('rotated', rot)    


#3. Resizeing an image
resz=cv.resize(img, (250,250), interpolation=cv.INTER_AREA)
#cv.imshow('resize', resz)


#4.Flipping of an image
flip = cv.flip(img, 1)
#cv.imshow('flipv', flip )
flip1 =cv.flip(img, 0)
#cv.imshow('flip1', flip1)
flip2 = cv.flip(img, -1)
#cv.imshow('flip2', flip2)


#5. Cropping of an image
crop = img[200:400, 0:100]
#             Y       X
cv.imshow('cropped', crop)

cv.waitKey(0)