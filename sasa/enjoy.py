class GPL:

    def __init___(self,nam,wgt,h):
        self.nam=nam
        self.wgt=wgt
        self.h=h

    def inp(self):
        self.nam=input("please enter your name?")
        self.wgt=input("Please enter your weight:")
        self.h=input("please enter your height(in metres)")

    def bmi(self):
        a=self.wgt
        b=self.height*self.height
        bmi=a/b
        return bmi
          
          


