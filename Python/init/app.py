# Printing first program

# print('Hello World')
# print("Sanjay")
# print('*' *10)

# Printing value from variables
# price = 10
# Value changes to 20
# price=20
# print(price)

# floating values
# rating = 5.9

# String value
# name = 'Sanjay'

# Boolean Value (Boolean True and False is Case sensitive)
# isTrue = True

# Excersice
# name = 'John Smith'
# age = 20
# newPatient = True

# getting input
# name=input("What is your name? ")
# fav_color=input('Wait which is your favorite color? ')
# print('Yeah! '+name+' likes '+fav_color)


# Type conversion

# birth_year=input('Birth Year :')
# print(type(birth_year))
# age=2019-int(birth_year)
# print(type(age))
# print(age)

# weight_kg=input('What is your weight in kg? ')
# weight_p=int(weight_kg)*2.20
# print('Your weight in pounds is '+ str(weight_p))

# name = 'SANJAY'
# print(name[2:-2])


# c='hello john'
# print(c)

# Printing or returning in multiple lines
# para='''
# Hello Sanjay,

# We recieved your mail.We will reach you soon.

# Thank you,
# The support team
# '''
# print(para)

# Slicing
# name='Malayalam'
# Reversing String
# print(name[::-1])
# Slicing
# print(name[0:4])
# Removing first and last character
# print(name[1:-1])
# Results

# malayalaM
# Mala
# alayala

# name ='Jennifer'
# print(name[1:-1])
# output - ennife


# first='SANJAY'
# last='MOHAN'
# message = first +' ['+last+'] '+'is a coder'
# Formated String
# formatted_message = f'{first} [{last}] is a coder'
# print(formatted_message)

# Sring Functions
# name= 'Sanjay is a coder'
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(5 % -3)
# print(-5 % 3)
# print(-5 % -3)
# print(-1 % 2)
# print(5-((5//-3)*-3))
# import math
# print(math.floor(2.9))
# isHot=False
# isCold=True
# if isHot:
#     print("It's a hot day")
#     print('Drink so much water')
# elif isCold:
#     print("It's a cold day")
#     print('Wear warm clothes')
# else:
#     print("It's a rainy day")
#     print('Take your Umberlla')
# print('Enjoy the day')

# good_credit=True
# if good_credit:
#     print("Your down payment is 1000$")
# else:
#     print("Your down payment is 2000$")
# high_income=False
# has_good_credit=True
# if has_good_credit and not high_income:
#     print("Hurray! YOU are eleigible for LOAN")
# name=input("What is your name? : ")
# if len(name)<3:
#     print('Enter a valid name :)')
# elif len(name)>50:
#     print('Enter a short name :)')
# else:
#     print(f'Huuray! Your Name is {name}')

# weight = input("Weight : ")
# unit = input("L for lbs & K for KG :")
# if unit.upper() == 'K':
#     weight = int(weight)*2.22
#     unit='lbs'
# elif unit.upper() =='L':
#     weight = int(weight)*0.45
#     unit='Kg'
# else:
#     print('Enter valid unit')
# print(f"You are {weight} {unit}")
# i=1
# while  i<=5:
#     print('*'*i )
#     i=i+1
# print("Done")


# SCRET GAME

# secret=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input('Guess : '))
#     guess_count +=1
#     if (guess==secret):
#         print('You Win!')
#         break
# else:
#     print('You Fail!')


# number = 100
# while number>0:
#     print(number)
#     number //=2


# count = 0
# for i in range(1,10):
#     if i % 2==0:
#         print (i)
#         count+=1
# print(f"Total of {count} numbers")


# def greet():
#     name =str(input("Let me know you name >>")).capitalize()
#     print(f"Hi {name}")
#     print("Welcome on board")


# greet()

# two type function
# 1 perform task
# 2 return a value


# def get_greeting(name):
#     return f"Hi {name}"

# message=get_greeting("sanjay")
# print(message)

# def sums(a,b):
#     print(a+b)
#     return a+b
# print(sums(5,6))

# def increment(number, value):
#     return number + value
# print(increment(6,value=2))
#  value=2 is a keyword argument which makes it easier to read the code

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j] == target:
#                 return [i,j]
#             else:
#                 pass
# print(twoSum([2,3,3],6))


# Default Arguments
# def increment(number,value=1):
#     return number+value

# print(increment(2))
# Get  default value one
# print(increment(2,3))


# XARGS

# def multiply(*numbers):
#     total = 1
#     for i in numbers:
#         total*=i
#     return total
# print(multiply(2,5,8,9))

# XXARGS
# def save_user(**user):
#     print(user)
#     print(user["name"])
#     print(user["id"])
#     print(user['age'])
# save_user(id=1,name="john",age=22)


# SCOPE
# Refers to region of code where a variable is defined
# inside a fuction defined variables are local variables 
# message="a"
# def greet(name):
#     message = "a"
# greet("Sanjay")
# print(message)
# def greets(name):
#     global message
#     message = "b"
# greets("Sanjay")
# print(message)


# Debugging
# Bug Code
# def multiply(*numbers):
#     total = 1
#     for i in numbers:
#         total*=i
#         return total
#  Refactored Code
# def multiply(*numbers):
#     total = 1
#     for i in numbers:
#         total*=i
#     return total
# print ("Start")
# print(multiply(2,5,8,9))


# FIZZ BUZZ 
# def fizz_buzz(input):
#     if input % 15==0:
#         return "Fizz Buzz"
#     elif input%3 == 0:
#         return "Fizz"
#     elif input%5 == 0:
#         return "Buzz"
#     return input
# n = int(input())
# for i in range(1,n+1):
#     print(fizz_buzz(i))


