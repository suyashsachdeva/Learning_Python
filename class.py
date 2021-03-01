#To make a class and store the the values in a list and then display them


class first:
    
    def __init__(self,nam='ss',age=18,marks=0):
        self.nam=nam
        self.age=age
        self.marks=marks

    def datask(self):
        self.nam=input("please enter your name")   
        self.age=input("please enter your age")  
        self.marks=input("please enter your marks")
          


    def info(self):
        print("Hello "+self.nam+" your age is "+str(self.age)+" and your marks are "+str(self.marks)) 



li=[]
no=int(input("please enter the number of student who want to enter their data"))
for x in range(no):
    dat1=first('suaysh',18,13)
    dat1.datask()
    li.append(first (dat1.nam, dat1.age, dat1.marks))


    print(li)
dat1.info()


"""       
i=int(input("enter the no. of students who have to send their info"))
for x in range(i):
    dat1.datask()
    a[i]=dat1.info()
"""    