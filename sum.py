list=[]
len=int(input("enter the length of the list"))
i=0
sum=0
while i<len:
    a=int(input("enter the number"))
    list.append(a)
    sum=sum+i
    print(list)
    i+=1
print(sum)
