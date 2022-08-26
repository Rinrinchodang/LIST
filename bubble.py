list=[7,70,12,18,21,17]
i=0
while i<len(list):
    j=0
    while j<len(list)-1:
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        j+=1
    i+=1
print(list)