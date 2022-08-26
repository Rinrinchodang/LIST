list=["p","q"]
n=5
i=1
b=0
a=[]
while i<=5:
    j=0
    while j<len(list):
        b=list[j]+str(i)
        a.append(b)
        j+=1
    i+=1
print(a)