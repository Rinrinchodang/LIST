list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
user=int(input("enter the number"))
i=0
while i<len(list):
    j=i
    while j<=user:
        if i==user:
            print(list[i-1])
        j+=1
    i+=1