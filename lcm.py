def lcm(x,y):
    if x>y:
        large=x
    else:
        large=y
    while 1:
        if ((large%x==0)and(large%y==0)):
            lcm=large
            break
        large=large+1

    return lcm

print(lcm(8,15))