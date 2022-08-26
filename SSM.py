elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+1
        sum=elements[i]+sum
    else:
        odd+=1
        sum1=elements[i]+sum1
    i+=1
avg=sum//even
avg1=sum1//odd
print("count",even)
print("count",odd)
print("sum",sum)
print("sum1",sum1)
print("no. of even numbers are=",avg)
print("no. of odd numbers are=",avg1)