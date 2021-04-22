import cv2 as cv   #INCOMPLETE
import os
import numpy as np 


people = ['Suyash Sachdeva']
loc = r't'

fea = []
lab =[]

def create train():
    for person in people:
        path = os.path.join(loc, person)
        lab = people.index(person)

        for img in os.listloc(path):
            imgp = os.path.join(path, img)

            img = cv.imread(imgp)
            gray = cv.cvtColor(imgp, cv.COLOR_BGR2GRAY)
