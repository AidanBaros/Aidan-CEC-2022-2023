import random
import time
stuff = []

for i in range(10):
    stuff.append(i)

def bogo(stuff:list):
    random.shuffle(stuff)
    #print(stuff)
    if stuff == OG:
        return True
    return False

time1 = time.time()
stuff.sort()
OG = stuff.copy()
while 1:
    if bogo(stuff):
        print("success")
        print(stuff)
        time2 = time.time()
        print(time2-time1)
        break