list=[1,7,3,10,8,12,43,5,]
a=[]
i=0
while i<len(list):
    j=[list[i],list[i+1]]
    a.append(j)
    i+=2
print(a)