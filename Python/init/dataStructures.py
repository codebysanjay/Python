number=list(range(1,20))
print(number[::2])
# Gives every second element after first element 

numbers=[1,2,3]
first=numbers[0]
second=numbers[1]
third=numbers[2]
# this is same as
first,second,third=numbers
# But here we should be sure that the number of items in list should be 
# equal to the number of variables on left
# Another way of unpacking
first,*others=numbers
print(first)
print(others)
# Here the except first element all other elements are stored in others-list



# LOOPING OVER LIST
letters=["a","b","c"]
for i in enumerate(letters):
    print(i)
# enumerate return a tuple with index,value

letters=["a","b","c"]
for index,letter in enumerate(letters):
    print(index,letter)
# UnPaackedTuple


# Adding and removing from list
lettersare=["a","b","c","d"]
print(lettersare,"The List")
# Adding at end
lettersare.append("f")
print(lettersare,"Added 'f' as a last element")
# Adding at position/index
lettersare.insert(2,"A")
print(lettersare,"added 'A' at position 2")
# Removing at index
lettersare.pop(0)
print(lettersare,"poped element at position 0")
# Removing specific character from list from first occurance
lettersare.remove("b")
print(lettersare,"removed first occurence of letter 'b'")
# Deleting range
del lettersare[0:2]
print(lettersare,"Removed range of letterr from 0 to 2")
# Delete all elements
lettersare.clear()
print(lettersare,"cleared the list")


# Finding Items
letterlist=["a","b","c","a"]
# Getting index of first occurence of element b
print(letterlist.index("b"))
# Getting number of occurence of  a character
print(letterlist.count("a"))


# Sorting List
numberslist=[5,8,2,4,5,7]
print(numberslist,"Orginal list")
print(sorted(numberslist),"Sorted using sorted")
print(numberslist,"Again Orginal list")
numberslist.sort()
print(numberslist,"Sorted Using sort list")
numberslist.sort(reverse=True)
print(numberslist,"sorted in reverse order using sort method")


# Sorting List of Tuples
items=[
    ("product1",8),
    ("product2",7),
    ("product3",12),
    ("product4",4)
]

def sortmedown(item):
    return item[1]
items.sort(key=sortmedown)
print(items)

# Using Lambda function an anonymous function creator
items.sort(key=lambda item: item[1])
print(items)

# Map Function
items=[
    ("product1",8),
    ("product2",10),
    ("product3",12),
    ("product4",4)
]
# Using Loops
price=[]
for item in items:
    price.append(item[1])
print(price)
# Using Map functon
temp=(map(lambda item:item[1],items))
for item in temp:
    print(item)
# Map to list 
temp=list(map(lambda item:item[1],items))
print(temp)


# Filter Function
print(list(filter(lambda item: item[1]>=10,items)))


# List Comprehension
# [expresion for item in items]
print([item for item in items if item[1]>=10])

# Zip Function
list1=[1,2,3]
list2=[10,20,30]
[(1,10),(2,20),(3,30)]
print(list(zip(list1,list2)))
# [(1, 10), (2, 20), (3, 30)]
print(list(zip("abc",list2)))
# [('a', 10), ('b', 20), ('c', 3)]


## STACKS ##
# Eg Browsing Session
browsing_session=[]
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
print(browsing_session.pop())
print(browsing_session)
print("redirect",browsing_session[-1])
browsing_session.pop()
browsing_session.pop()
if not browsing_session:
    print("disabled back button")
# This Will only return the value untill the browsing_session become empty
# When browsing_session become empty not browsing_session will return a true boolean



## QUEUE ##
# Queue in real world
# Dequeue for long queue
from collections import deque
queue=deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
queue.popleft()
queue.popleft()
if not queue:
    print("empty")


# # TUPLES # #
#  Tuple is a read only list , cannot modify objects in it
point=1
# An integer
point=1,
# Treats as a tuple
point=1,2
# Returns a tuple
point=()
Empty tuple
# can concatenate, multiply tuples
# csn covert list to tuple
point=tuple(["hello world"])
# Swapping Variables
x=10
y=11
# Swap in python as a tuple
x,y=y,x

# Swapping two number without third
x=x+y
y=x-y
x=x-y
print("X = ",x,"\nY = ",y)


# # ARRAYS # #
from array import array
# On;y used if large number of elements are there say greater than 10000
numbers=array("i",[1,2,3])
print(numbers)
print(type(numbers))


