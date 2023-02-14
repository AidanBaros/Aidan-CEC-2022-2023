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

def four(x,y,z=0,a=0):
    if x < y:
        return four(y,x,z)
    z+=1
    a = y/z
    if a%2 == 0:
        if x%a == 0:
            return a
        else:
            return four(x,y,z)
    else:
        return four(x,y,z)

def fourb(x:int,y):
    if x < y: x, y = y, x
    for i in range(x):
        z = x - i
        if x%z == 0 and y%z == 0:
            return z

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

def six(x,y=[1],z=[1]):
    y = z.copy()
    if x == 0:
        return ""
    print(y)
    for i in range(len(y)+1):
        if i == len(y):
            z.append(1)
        elif i == 0:
            z[0] = 1
        else:
            z[i] = int(y[i]) + int(y[i-1])
    x -= 1
    return six(x,y,z)

def sixb(x):
    pascal = []
    NewPascal = [1]
    for j in range(x):
        pascal = NewPascal.copy()
        print(NewPascal)
        for i in range(len(pascal)+1):
            if i == len(pascal):
                NewPascal.append(1)
            elif i == 0:
                pass
            else:
                NewPascal[i] = int(pascal[i]) + int(pascal[i-1])
        
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
    y = int(input("4: "))
    z = int(input("4: "))
    print(four(y,z))
elif x == "4b":
    y = int(input("4b: "))
    z = int(input("4b: "))
    print(fourb(y,z))
elif x == "5":
    y = input("5: ")
    print(five(y))
elif x == "5b":
    y = input("5b: ")
    print(fiveb(y))
elif x == "6":
    y = int(input("6: "))
    print(six(y))
elif x == "6b":
    y = int(input("6b: "))
    sixb(y)
else:
    print("Not an option")

