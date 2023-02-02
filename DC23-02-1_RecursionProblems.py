def one(x: int, y: int = 0) -> int:
    y = x + y
    if x == 0:
        return y
    else:
        return one(x-1,y)

def two():
    pass


x = int(input("which one? : ")
)
if x == 1:
    y = int(input("give me a number and i will give you your sum of its parts. : "))
    print(one(y))
    
if x == 2:
    pass
if x == 3:
    pass
if x == 4:
    pass
if x == 5:
    pass
if x == 6:
    pass

