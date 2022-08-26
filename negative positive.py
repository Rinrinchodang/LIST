l=[-5,-7,12,17,5,9,10,16,20,-17]
i=0
negative=0
positive=0
sum=0
sum1=0
while i<len(l):
    if l[i]>0:
        positive+=1
        sum=sum+l[i]
    else:
        negative+=1
        sum1=sum1+l[i]
    i+=1
print(sum)
print(sum1)


    