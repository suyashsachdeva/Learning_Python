import cv2 as cv      #This uses edges to detect faces so their is no involvement to color


link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                #program is incomplete and need to be updated
cv.imshow('gray', gray)


harcas = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_casacade.detectMultiScale(gray, scaleFactor=1.1, minNeighors = 3)  #The last two factors can be manucilated to get the desired 
                                                                                    #sensitivity for detecting faces 
print("NO. of faces detected are"+len(face_rect))

for (x,y,w,h) in face_rect:                                             #This loop is their to basically form a triangle
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)                    

cv.imshow('detected Face', img)








cv.waitKey(0)