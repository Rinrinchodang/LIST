i=1
a=[]
while i<=30:
    count=0
    j=2
    while j<=i//2:
        if i%j==0:
            count=count+1
        j+=1
    if count==0 and i!=1:
        a.append(i)
    i+=1
print(a[0:5])
print(a[6:10])


