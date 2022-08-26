marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
]
sum=0
i=0
while i<len(marks):
    j=0
    total=0
    while j<len(marks[i]):
        total=marks[i][j]+total
        j+=1
    sum=sum+total
    i+=1
print(sum)

