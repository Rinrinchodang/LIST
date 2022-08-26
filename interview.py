name=["neha","pooja","deepti","chandani","preeti","rani"]
i=0
while i<len(name):
    a=0
    while a<len(name[i]):
        room=int(input("enter the number:"))
        if room==1:
            print("neha","pooja")
        elif room==2:
            print("deepti","chandani")
        else:
            print("preeti","rani")
        a+=1
    i+=1

name=["neha","pooja","deepti","chandani","preeti","rani"]
i=0
room=[1,2,3]
while i<len(room):
    print(room,"room"[i])
    a=1
    j=0
    while j<len(name[i]):
        print(a,".",name[j])
        # room.append(name)
        a+=1
        j+=1
    i+=1
    
    # print(room,"room[i]")

       