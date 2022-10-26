def Fibonacci(a,b,c):
    print(a)
    if a > c:
        return
    return Fibonacci(b,(a+b),c)

Fibonacci(0,1,10000)


