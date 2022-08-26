list=["1","2","3","4","5","6"]
i=0
str=""
a=[]
while i<len(list):
    str=list[i]+list[i+1]
    a.append(str)
    i+=2
print(a)
