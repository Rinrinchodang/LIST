list=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
str=""
while i<len(list):
    j=0
    while j<len(list[i]):
        str=str+list[i][j]
        j+=1
    i+=1
print(str)