magic_square=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
i=0
a=0
b=0
c=0
while i<len(magic_square):
    a=a+magic_square[i][0]
    b=b+magic_square[i][1]
    c=c+magic_square[i][2]
    i+=1
    print(a,b,c)
if a==b==c:
    print("magic number")
else:
    print("not a magic number")