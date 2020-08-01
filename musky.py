for row in range(0,5):
    for col in range(0,9):
        if(row==0 or row==1 or ((col==0 or col==1) and (row!=0 or row!=1)) or ((col==7 or col==8 ) and (row!=0 or row!=1))):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
for row in range(0,2):
    for col in range(0,9):
        if(col==0 or col==1 or col==7 or col==8):
            print(" ",end=" ")
        else:
            print(end=" ")
    print()
for row in range(0,5):
    for col in range(0,9):
        if(row==3 or row==4 or ((col==0 or col==1) and (row!=3 or row!=4)) or ((col==7 or col==8 ) and (row!=3 or row!=4))):
            print("*",end=" ")
        else:
            print(end=" ")
    print()        