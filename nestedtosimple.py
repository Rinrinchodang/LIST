n=[2,3,4,[4,2,4],[6,["a","b"],3],[1,4]]
i=0
a=[]
while i<len(n):
    if type (n[i])==type([]):
        j=0
        while j<len(n[i]):
            if type (n[i][j])==type([]):
                k=0
                while k<len(n[i][j]):
                    a.append(n[i][j][k])
                    k+=1
            else:
                a.append(n[i][j])
            j+=1
    else:
        a.append(n[i])
    i+=1
print(a)

list=[[1,2,3],[4,5,6],7,[8,9,10]]
b=[]
i=0
while i<len(list):
    if type(list[i])==type([]):
        j=0
        while j<len(list[i]):
            b.append(list[i][j])
            j+=1
    else:
        b.append(list[i])
    i+=1
print(b)