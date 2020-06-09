def caesarcipher(msg,num):
    result = " "
    for char in msg:
        if char == ' ':
            result = result + char
        elif (char.isupper()):
            result+=chr((ord(char)+num-65)%26+65)
        else:
            result+=chr((ord(char)+num-97)%26+97)
    return result
msg=input(print("Enter msg: "))
num=int(input(print("enter shift number: ")))
print("The message given is : ",msg)
print("The shift value is : ",num)
print("The Encrypted msg is :"+ caesarcipher(msg,num))
