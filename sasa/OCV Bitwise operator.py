import cv2 as cv
import numpy as np 

blank = np.zeros((400,400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cir = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rect)
cv.imshow('circle', cir)


#1. AND
bitand = cv.bitwise_and(rect, cir)
cv.imshow('AND', bitand)

#2. OR
bitor = cv.bitwise_or(rect, cir)
cv.imshow('OR', bitor)

#3. XOR(non-intersecting regions of the two figures)
bitxor = cv.bitwise_xor(rect, cir)
cv.imshow('XOR', bitxor)

#4. NOT
bitnot = cv.bitwise_not(rect)
cv.imshow('NOT', bitnot)





cv.waitKey(0)