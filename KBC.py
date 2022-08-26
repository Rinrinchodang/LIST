question_list=[
    ["how many continents are there?"],
    ["what is the capital of india?"],
    ["NG mei kaun se course padhaya jaata hai?"]
]
options_list=[
    ["four","nine","seven","eight"],
    ["chandisgarh","bhopal","chennai","delhi"],
    ["software engineering","counseling","tourism","agriculture"]
]
life_line=[
    ["seven","eight"],
    ["bhopal","delhi"],
    ["software engineering","counselling"]
]
life_line=[["seven","eight"],["bhopal","delhi"],["software engineering","counseling"]]
solution_list2=[1,2,1]
i=0
count=0
solution_list=[3,4,1]
while i<len(question_list):
    print("q",(i+1),question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j+=1
    user=("without lifeline","with lifeline")
    print("choose your choice:")
    print("1.without lifeline")
    print("2.with lifeline")
    choice=int(input("your choice"))
    if choice==1:
        user1=int(input("enter your choice:"))
        if user1==solution_list[i]:
            print("congrates")
        else:
            print("wrong answer")
            break
    elif choice==2:
        if count==0:
            k=0
            while k<len(life_line[i]):
                print(k+1,life_line[i][k])
                k+=1
            count+=1
            user2=int(input("enter your answer:"))
            if user2==solution_list2:
                print("congratulation")
            else:
                print("wrong answer,please try next time")
                break
        elif choice==1:
            print("you have used your life_line")
            if count==1:
                l=0
                while l<len(solution_list[i]):
                    print(l+1,solution_list[i][l])
                    l+=1
                count=count+1
                user3=input("enter your choice")
                if user3==solution_list[i]:
                    print("wow")
                else:
                    print("sorry")
                    break
        else:
            print("you have used your life_line")
            user4=int(input("enyter your answer"))
            if user4==solution_list[i]:
                print("bravo")
            else:
                print("wrong answer")
                break
    else:
        print("sorry,wrong answeer")
        break
    i+=1

            #         print("congrates")
#     elif user==5050:
#         if count==0:
#             k=0
#             while k<len(life_line[i]):
#                 print(k+1,life_line[i][j])
#                 k+=1
#             count+=1
#             user2=int(input("enter the number"))
#             if user2==solution_list2[i]:
#                 print("correct")
#             else:
#                 print("wrong")
#         else:
#             print("you already use 5050 chances")
#             num=int(input("enter the number:"))
#             if num==solution_list[i]:
#                 print("right answer")
#                 break
#     else:
#         print("your answer is wrong")
#         break
#     i+=1

        
