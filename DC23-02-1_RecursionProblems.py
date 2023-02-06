import math
# b is for better because some of these would be better without recursion


def one(x: int, y: int = 0) -> int:
    y = x + y
    if x == 0:
        return y
    else:
        return one(x-1,y)
    
def oneb(x):
    total = 0
    for i in range(x):
        total += x - i 
    return total

def two(x,y,z=0):
    if z == 0:
        z = x
    z = x * z
    if y <= 2:
        return z
    else:
        return two(x,y-1,z)

def twob(x,y):
    return x**y

def three(x:str,y=0,z=0):
    if y == 0 and z == 0:
        y = len(x)
    elif y == 0:
        return z
    z += int(x[y-1])
    y -= 1
    return three(x,y,z)

def threeb(x):
    total = 0
    for num in x:
        total += int(num)
    return total

def four(x,y,z):
    pass

def five(x:str,y:str="",z=0):
    if z == 0 and y == "":
        z = len(x)
    elif z == 0:
        return y
    y = y + x[z-1]
    z -= 1
    return five(x,y,z)

def fiveb(x):
    return x[::-1]

def six(x,y,z):
    pass




x = input(" -- ")

if x == "1":
    y = int(input("1: "))
    print(one(y))
elif x == "1b":
    y = int(input("1b: "))
    print(oneb(y)) 
elif x == "2":
    y = int(input("2: "))
    z = int(input("2: "))
    print(two(y,z))
elif x == "2b":
    y = int(input("2b: "))
    z = int(input("2b: "))
    print(twob(y,z))
elif x == "3":
    y = input("3: ")
    print(three(y))
elif x == "3b":
    y = input("3b: ")
    print(threeb(y))
elif x == "4":
    pass
elif x == "4b":
    pass
elif x == "5":
    y = input("5: ")
    print(five(y))
elif x == "5b":
    y = input("5b: ")
    print(fiveb(y))
elif x == "6":
    pass
elif x == "6b":
    pass
else:
    print("Not an option")

