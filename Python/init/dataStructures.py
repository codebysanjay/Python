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

# Using Lambda function
items.sort(key=lambda item: item[1])
print(items)