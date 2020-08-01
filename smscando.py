#STUDENT MANAGEMENT SYSTEM
print("****** WELCOME TO STUDENTS SECTION*******")

class student:
    def __init__(self,prn):
        self.prn=prn
        
            
    def roll(self):
        prn=self.prn
        roll_no=prn%100
        return roll_no    
    def batch(self):
        roll_no=self.roll()
        if(roll_no<=20):
            bat='a'
            return bat
        elif(roll_no<=40 and roll_no>=21):
            bat='b'
            return bat
        elif(roll_no<=60 and roll_no>=41):
            bat='c'
            return bat
        else:
            print(" wrong roll_no")
la=[]
lb=[]
lc=[]
while(1):
    print("1:insert\n2:display\n3:exit")
    ch=int(input("******* enter your choice*********"))
    if(ch==1):
        name=input("******ENTER YOUR NAME*****")
        gender=input("******ENTER YOUR GENDER*********")
        prn=int(input("******** ENTER YOUR PRN NO**********")) 

        obj=student(prn)
        roll_no=obj.roll()
        
        bat1=obj.batch()
        if(bat1=='a'):
            la.append(roll_no)
            la.append(prn)
            la.append(name)
            la.append(gender)
            la.append(bat1)
        elif(bat1=='b'):
            lb.append(roll_no)
            lb.append(prn)
            lb.append(name)
            lb.append(gender)
            lb.append(bat1)
        elif(bat1=='c'):
            lc.append(roll_no)
            lc.append(prn)
            lc.append(name)
            lc.append(gender)
            lc.append(bat1)
    if(ch==2):
        print(la)
        print(lb)
        print(lc)
            
    if(ch==3):
        exit(0)        
                    