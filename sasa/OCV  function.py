import cv2 as cv

def rescale(frame,scale=0.17):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


path=r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
img = cv.imread(path)

frame=rescale(img)
cv.imshow('nailed it finally', frame)

#1. Converting the image to black and white
gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)


#2. Bluring the image
blur = cv.GaussianBlur(frame, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)


#3. Edges in a image
canny=cv.Canny(frame, 125, 175)
#cv.imshow('Canny Edges', canny)

#3.1 Reduce the number of edges
cannyb=cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edges blur', cannyb)


#4. Dilating the image(colors ko ubhar ke bahar nikalta he and jyada number of iteration ho to image mc jati he)
dil = cv.dilate(cannyb, (3,3), iterations=3)
#cv.imshow('dilated', dil)
dila = cv.dilate(frame, (3,3), iterations=10)
#cv.imshow('dilateda', dila)


#5. Reverse of Dilation to erode
erod1 = cv.erode(dil, (3,3), iterations=3)
#cv.imshow('eroded image', erod1)
erod2 = cv.erode(cannyb, (3,3), iterations=1)
#cv.imshow('eroded image2', erod2)
erod3 = cv.erode(frame, (3,3), iterations=3)
#cv.imshow('eroded image3', erod3)


#6. Resizing of a image(statement version)
resz1 = cv.resize(img, (10,10), interpolation=cv.INTER_AREA)
#cv.imshow('resizing of a image1', resz1)

#These two are used to make ana image bigger and in the cubic is slow but gives the best quality

resz2 = cv.resize(img, (1000,700), interpolation=cv.INTER_LINEAR)
#cv.imshow('resizing of a image2', resz2)
resz3 = cv.resize(img, (1000,700), interpolation=cv.INTER_CUBIC)
#cv.imshow('resizing of a image3', resz3)


#7. Cropping of a image
crop = img[0:700, 0:500]
cv.imshow('cropped', crop)



cv.waitKey(0)