list=[27,10,30,10,5,5]
a=[]
i=0
while i<len(list):
    j=[list[i]-list[i+1]]
    a.append(j)
    i+=2
print(a)


