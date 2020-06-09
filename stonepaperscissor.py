import random
print("Winner Is decided by the following Rules :\n"
      +"Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      +"paper vs scissor->scissor wins \n")

while True:
        print("Enter the Choice : \n 1. Rock\n 2. Paper\n 3.scissor")
        choice=int(input("User Turn: "))
        while choice > 3 or choice < 1 :
            choice=int(input("Enter valid choice :"))
        if choice==1:
                choice_name="Rock"
        elif choice==2:
                choice_name="Paper"
        else:
                choice_name="Scissor"


        print("User Choice is : "+ choice_name)
        print("\n Now Computers Turn.....")
        comp_choice=random.randint(1,3)
        while comp_choice==choice:
            comp_choice=random.randint(1,3)


        if comp_choice==1:
            comp_choice_name="Rock"
        elif comp_choice==2:
            comp_choice_name="Paper"
        else:
            comp_choice_name="Scissor"

        print("Computers Choice is : "+comp_choice_name)
        print("\n"+choice_name + "  --V/S--  " + comp_choice_name)

        if ((choice==1 and comp_choice==2)or(choice==2 and comp_choice==1)):
                print("Paper Wins =>",end=" ")
                result="Paper"
        elif ((choice==1 and comp_choice==3)or(choice==3 and comp_choice==1)):
                print("Rock Wins =>",end=" ")
                result="Rock"
        else:
                print("Scissor Wins =>",end=" ")
                result="Scissor"


        if result==choice_name:
                print("<=User Wins=")
        else:
                print("<=Computer Wins=>")

        print("Do you want to play again? Y/N")
        ans=input()

        if ans=='n' or ans=='N':
                break


print("Thanks For Playing")