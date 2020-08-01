# CAR INSUARANCE SYSYEM
def car_type():
    print(" CARS WE COVER\n1:Hadchback\n2:Sedan\n3:SUV")
    ch1=int(input("Enter your choice\n"))
    if(ch1==1):
        return 'Hadchback'
    elif(ch1==2):
        return 'Sedan'
    elif(ch1==3):
        return 'SUV'
    else:
        print("WRONG CHOICE")
    
    
def engine_capacity():
    print("ENGINE CAPACITY\n1:<1000cc\n2:<2000cc\n3:<3000cc")
    ch2=int(input("Enter your choice\n"))
    if(ch2==1):
        return '<1000cc'
    elif(ch2==2):
        return '<2000cc'
    elif(ch2==3):
        return '<3000cc'
    else:
        print("WRONG CHOICE")
    
    
    
def price_range():
    print("PRICE RANGE\n1:500000-600000\n2:600001-700000\n3:700001-800000\n4:800001-900000\n5:900001-1000000\n6:1000001-1100000\n7:1100001-1200000")
    ch3=int(input("Enter your choice\n"))
    if(ch3==1):
        return '500000-600000'
    elif(ch3==2):
        return '600001-700000'
    elif(ch3==3):
        return '700001-800000'
    elif(ch3==4):
        return '800001-900000'
    elif(ch3==5):
        return '900001-1000000'
    elif(ch3==6):
        return '1000001-1100000'
    elif(ch3==7):
        return '1100001-1200000'
    else:
        print("WRONG CHOICE")
    
def time():
    print("TIME IN YEARS\n1:1-2yrs\n2:2-3yrs\n3:3-4yrs\n4:4-5yrs\n")
    ch4=int(input("Enter your choice\n"))
    if(ch4==1):
        return '1-2'
    elif(ch4==2):
        return '2-3'
    elif(ch4==3):
        return '3-4'
    elif(ch4==4):
        return '4-5'
    else:
        print(" INVALID CHOICE")
    
def discount():
    print("DISCOUNT IN %\n1:5\n2:10\n3:15\n4:20\n")
    ch5=int(input("Enter your choice\n"))
    if(ch5==1):
        return '5'
    elif(ch5==2):
        return '10'
    elif(ch5==3):
        return '15'
    elif(ch5==4):
        return '20'
    else:
        print(" INVALID CHOICE")
    
    
def insuarance_type():
    print("INSUARE TYPE\n1:Third Party\n2:Own Damage Cover\n3:Comprehensive")
    ch6=int(input("Enter your choice\n"))
    if(ch6==1):
        return 'Third Party'
    elif(ch6==2):
        return 'Own Damage Cover'
    elif(ch6==3):
        return 'Comprehensive'
    else:
        print("WRONG CHOICE")
        
def calculator():
    cartype=car_type()
    enginecapacity=engine_capacity()
    pricerange=price_range()
    
    
    insuarancetype=insuarance_type()
    price=int(input("What is the price of the car (500000-1200000)\n"))
    acc=int(input("What is the price of the accessories\n"))
    if(enginecapacity=='<1000cc'):
        tp=2055
    elif(enginecapacity=='<2000cc'):
        tp=2863
    elif(enginecapacity=='<3000cc'):
        tp=7890
    tim=time()
    if(tim=='1-2'):
        dp=0.1*price
    elif(tim=='2-3'):
        dp=0.2*price
    elif(tim=='3-4'):
        dp=0.3*price
    elif(tim=='4-5'):
        dp=0.4*price
    discoun=discount()
    if(discoun=='5'):
        bonus=0.05*price
    elif(discoun=='10'):
        bonus=0.1*price
    elif(discoun=='15'):
        bonus=0.15*price
    elif(discoun=='20'):
        bonus=0.2*price
        
   
    
    
    IDV=price+acc-dp
    odc=IDV-bonus    
    if(insuarancetype=='Third Party'):
        total=tp
    elif(insuarancetype=='Own Damage Cover'):
        total=odc
    elif(insuarancetype=='Comprehensive'):
        total=tp+odc
    print("TOTAL AMOUNT",total)    
        
        
        
                
        
    
    
                
        
# FUNCTION CALLING START

l=[]
calculator()



      
        