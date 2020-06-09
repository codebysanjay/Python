def fib(a):
    if a<=1:
        return a
    else:
        return(fib(a-1)+fib(a-2))


for i in range (9):
    print(fib(i))
