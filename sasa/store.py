"""print("hello my name is suyash")
i=0
li=[]
a=int(input("Please enter the number of names you want to store"))
u=[x for x in input("Enter"+str(a)+"name").split()]
if len(u)>a:
    if a<=len(u)+1:
        del u[a] 
        a+=1      
print(u)"""    
#program 2
"""
def fun(x):
    if x==0:u=0
    elif x==1:u=1
    else:
        u=fun(x-1)+fun(x-2)    
    return u
a=int(input("plz enter a number")) 
print(fun(a))   
"""

#program 3
"""
class data:
    
    def __init__(self,nam,marks,age):
            self.nam=input("enter your name:")
            self.marks=input("enter your marks:")
            self.age=input("enter your age:")
            

    @staticmethod
    def display():
        num=0
        while num<a:
            print("Name:"+nam+"Marks:"+marks+"Age:"+age)

a=int(input("Enter the number of students whose data  be stored "))
for i in range(a):
"""


#program 4
"""
import pickle
class Student:
    def __init__(self,id,name,test):
        self.id=id
        self.name=name
        self.test= test

    def display(self):
        print(self.id,self.name,self.test)

f=open("student.dat","wb")
s=Student("123","Sasa","55")
pickle.dump(s,f)
f.close()

f=open("student.dat","rb")
obj=pickle.load(f)
obj.display()
f.close()
"""
#program 5
"""
from threading import*

class bus:

    def __init__(self,aseat):
        self.aseat=aseat
        self.l=Lock()

    def buy(self,rseat):
        self.l.acquire()

        if(self.aseat>=rseat):
            print("number odf available seats:",self.aseat)
            print("confirmation a seat ")
            print("Processing the ticket ")
            print("Printing the ticket ")
            self.aseat-=rseat
        else : print("sorry their are only "+str(self.aseat)+" seats available")
        self.l.release()
obj=bus(20)
a=input("please enter the no. of seats u want to book")
for i in range(len(a)):
    t1=Thread(target=obj.buy,args=(int(a),))
t2=Thread(target=obj.buy,args=(b,))
t3=Thread(target=obj.buy,args=(c,))    

t1.start()
t2.start()
t3.start()
"""

 #program 6 
"""       
import socket

host='localhost'
port=4000
s=socket.socket()
s.bind((host,port))
print("Server listening on port:",port)
s.listen(1)

c,addr = s.accept()

print("Connection from:",str(addr))

c.send(b"Hello, how are you")
c.send("bye".encode())
c.close()
"""
"""
#program 7

import socket

host='localhost'
port=6969

s=socket.socket()
s.bind((host,port))
print("server listening on the port")
s.listen(1)

c,addr = s.accept()

file= c.recv(1024)

try:
    f=open(file,'rb')
    content=f.read()
    c.send(content)
    f.close()
except:
    c.send(b"file does not exist")
"""
# program 8


