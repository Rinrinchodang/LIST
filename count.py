list=['a','a',5,4,4,5]
i=0
a=[]
while i<len(list):
    c=0
    j=0
    b=[]
    while j<len(list):
        if list[i]==list[j]:
            c+=1
        j+=1
    b.append(list[i])
    # b.append("=")
    b.append(c)
    # c="".join(b)
    if b not in a:
        a.append(b)
    i+=1
print(a)
# i=0
# while i<len(list):
#     b=list.count("a")
#     d=list.count(5)
#     e=list.count(4)
#     i+=1
# print("a =",b,"times")
# print("5 =",d,"times")
# print("4 =",e,"times")