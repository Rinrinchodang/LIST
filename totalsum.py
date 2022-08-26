number=30
n=[10,11,12,13,14,17,18,19]
sum=0
a=[]
i=0
while i<len(n):
    j=0
    while j<i:
        if n[j]+n[i]==number:
            b=n[j],n[i]
            a.append(b)
            a.sort()
        j+=1
    i+=1
print(a)