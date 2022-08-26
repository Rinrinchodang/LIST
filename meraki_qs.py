numbers=[50,40,23,70,56,12,5,10,7]
count=0
while numbers[count:]:
    count+=1
print(count)

numbers=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(numbers):
    if numbers[i]>=20 and numbers[i]<=40:
        count+=1
    i+=1
print(count)

numbers=[50,40,23,70,56,12,5,10,7]
i=0
max=numbers[0]
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i+=1
print(max)

numbers=[50,40,23,70,56,12,5,10,7]
i=0
second_max=numbers[0]
largest=numbers[0]
while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    if numbers[i]>second_max and numbers[i]!=largest:
        second_max=numbers[i]
    i+=1
print(second_max)

places=["delhi","gujarat","rajasthan","punjab"]
i=-1
while i>=(-(len(places))):
    print(places[i])
    i-=1

name=['n','i','t','i','n']
i=-1
a=[]
while i>=(-(len(name))):
    a.append(name[i])
    i-=1
if a==name:
    print("palindrome")
else:
    print("not palindrome")


list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
i=0
a=[]
while i<len(list1):
    if list1[i] not in list2:
        a.append(list1[i]) 
    i+=1
print(a)

elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
while i<len(elements):
    if elements[i] %2==0:
        print("even number")
    else:
        print("odd number")
    i+=1

elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
c1=0
c=0
a=[]
b=[]
while i<len(elements):
    if elements[i] %2==0:
        c1+=1
        a.append(elements[i])
    elif elements[i]%2!=0:
        c=c+1
        b.append(elements[i])
    i=i+1
print("even",c1)
print("odd",c)
    
elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even=0
odd=0
sum=0
sum1=0
while i<len(elements):
    if elements[i] %2==0:
        even+=1
        sum+=elements[i]
    else:
        odd+=1
        sum1+=elements[i]
    i+=1
print(sum)
print(sum1)
