print("Input your three favorite bands")
temp = []
for i in range(3):
    inp = input(" -- ")
    temp.append(inp)


tuple1 = tuple(temp)

print(tuple1[1])


print("Input your five favorite foods")
temp = []
for i in range(5):
    inp = input(" -- ")
    temp.append(inp)


tuple1 = tuple(temp)

print(tuple1[-1])


print("Input your six favorite video game hero/villian pairs (i.e. Mario and Bowser)")
dict = {}
for i in range(6):
    inpH = input("Hero -- ")
    inpV = input("Villian -- ")
    dict[inpH] = inpV

print(dict)
print(dict.get("a"))
