l=int(input("enter length \n" ))
b=int(input(" enter breadth \n "))
class muskan:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def rect(self):
        area=self.l*self.b
        print("area=",area)
taran=muskan(l,b)
taran.rect()
      