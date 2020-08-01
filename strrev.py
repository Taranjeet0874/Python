l=[]
l=[1,2,3,4,5,6]
print(l)
for i in range(4,0,-1):
    l.append(l[i])
print(l)    
for i in range(0,5):
    del(l[i])
print(l)    