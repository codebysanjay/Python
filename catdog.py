def cd(str):
    num1=0
    num2=0

    if "dog" and "cat" not in str:
        return True
    for i in range (len(str)-2):
        if str[i:i+3]=="cat":
            num1+=1
        if str[i:i+3]=="dog":
            num2+=1

    if num1==num2:
       return True
    else:
        return False

msg=input(print("Enter the string :"))

print("")
print("")
print("After checking the answer is : ",cd(msg))


