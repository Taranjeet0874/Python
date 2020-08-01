file=open("tfs.txt",'w')
file.write("hello")
file.write("how are you")
file.close()
file=open("tfs.txt","r")
myfi=file.read()
list1=myfi.split()
lengthoflist=len(list1)
reg_no=3
count=3

vehicles=[]
class tfs:

    def register(self):
        global count
        global reg_no
        reg_no=str(reg_no)
        reg_no=3+ count
        count=count+1
        
        name=input("enter name : ")
        v_no=int(input("enter vehicle number : "))
        v_no=str(v_no)
        reg_no=str(reg_no)
        record=open("tfs.txt","a")
        temp_rec_str=(reg_no+"\t\t\t"+name+"\t\t\t"+v_no+"\n")
        record.write(temp_rec_str)
        print("registration done.")
        print("registration no.       vehicle               vehicle number")
        record.close()
        
    def display(self):
        record=open("tfs.txt","r")
        recs=record.read()
        print(recs)
        record.close()

    record=open("tfs.txt","w")
    record.write("registration no\t\t\tvehicle\t\t\tvehicle no\n")

    def search(self):
        
        print("search by    1. vehicle number    2.vehicle name : ")
        ch=int(input("enter your choice : "))
        reg_v=[1234,2345,3456]
        lenreg_v=len(reg_v)      
        reg_vehicle=['bike','car','truck']  
        lenreg_vehicle=len(reg_vehicle)
        if(ch==1):
            Id=int(input("enter number : "))
            for i in range(0,lenreg_v):
                if(reg_v[i]==Id):
                    print("vehicle found")
                    
        elif(ch==2):
            name=input("enter name : ")
            for i in range(0,lenreg_vehicle):
                if(reg_vehicle[i]==name):
                    print("vehicle found")
                    

    def fine(self):
        vn=input("enter vehicle name : ")
        if(vn=='bike'):
            print("your fine is 500 ")
        elif(vn=='car'):
            print("your fine is 1000")
        elif(vn=='truck'):
            print("your fine is 1500")
obj=tfs()
while(1):
    print("enter\n 1. to register \n 2. search \n3. fine")
    ch=int(input("enter your choice : "))
    if(ch==1):
        obj.register()
        obj.display()
    elif(ch==2):
        obj.display()
        obj.search()    
    elif(ch==3):
        obj.fine()
    else:
        break


        