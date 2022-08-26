list=["ramchanphy","pooja"]
str=""
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]==list[i][0]:
            x=list[i][0].upper()
            str+=x+"."
        j+=1
    i+=1
print(str[0:3])