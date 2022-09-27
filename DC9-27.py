import time

inp = list(input("Input a 4 charicter password -- "))
start = time.perf_counter()

for i, c in enumerate(inp):
    inp[i] = ord(c)

guess = list(32 for val in range(len(inp)))

while True:
    if guess == inp:
        end = time.perf_counter()
        break
    guess[0] += 1
    for i in range(len(inp)):
        if guess[i] % 127 == 0:
            guess[i] = 32
            guess[i+1] += 1

    
print(round(end - start, 1))
print(guess)
