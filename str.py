list=["hello","world","this","is","great"]
# x=" ".join(list)
# i=0
# while i<len(x):
#     i+=1
# print(x)

i=0
str=""
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]==list[i][0]:
            x=str+list[i]
            str+=list[i]+" "
        j+=1
    i+=1
print("'"+x+"'")

