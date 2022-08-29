import pygame
import random
pygame.init()
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

def q1():
    x = input("type a number -- ")
    if (int(x)%3) == 0: print("boogers")
    else: print("squirrels")

def q2():
    for i in range(10,31,5):
        print(i)

def q3():
    def midpoint(x1,y1,x2,y2):
        midx = (x1+x2)/2
        midy = (y1+y2)/2
        print("the midpoint of your points is", str(midx)+", "+ str(midy))
    print("enter 2 x and y positions")
    x1 = input("first x pos -- ")
    y1 = input("first y pos -- ")
    x2 = input("second x pos -- ")
    y2 = input("second y pos -- ")
    midpoint(int(x1),int(y1),int(x2),int(y2))

def q4():
    ListONames = []
    MoInList = False
    print("enter 5 names")
    for i in range(5):
        x = input(" -- ")
        ListONames.append(x)
    ListONames.sort()
    for j in range(5):
        if ListONames[j].lower() == "mo":
            MoInList = True
    if MoInList == True:
        print("nerd alert")
    else:
        print("cool kids only")

def q5():
    class ant():
        def __init__(self,q,c):   
            self.XPos = 50
            self.YPos = 50
            self.Queen = q
            self.color = c
        def antData(self):
            print("Position - ",self.XPos,",",self.YPos ,"\nQueen - ",self.Queen,"\nColor - ",self.color)

        def bark(self):
            print("woof")

        def move(self):
            randX = random.randint(-5,5)
            randY = random.randint(-5,5)
            xPos = (self.XPos + randX)
            yPos = (self.YPos + randY)
            self.XPos = xPos
            self.YPos = yPos

    a1 = ant(True,RED)
    a1.bark()
    a1.move()
    a1.antData()

    a2 = ant(False,GREEN)
    a2.bark()
    a2.move()
    a2.antData()

    a3 = ant(False,BLUE)
    a3.bark()
    a3.move()
    a3.antData()
            
def q6():
    class ant():
        def __init__(self,q,c):   
            self.XPos = 50
            self.YPos = 50
            self.Queen = q
            self.color = c
        def antData(self):
            print("Position - ",self.XPos,",",self.YPos ,"\nQueen - ",self.Queen,"\nColor - ",self.color)

        def bark(self):
            print("woof")

        def move(self):
            randX = random.randint(-5,5)
            randY = random.randint(-5,5)
            xPos = (self.XPos + randX)
            yPos = (self.YPos + randY)
            self.XPos = xPos
            self.YPos = yPos

        def draw(self):
            pygame.draw.rect(screen,(self.color),(self.XPos,self.YPos,10,5))

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("ANT")

    doExit = False
    clock = pygame.time.Clock()

    while not doExit:
    
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doExit = True

        a1 = ant(True,RED)
        a1.bark()
        a1.move()
        a1.antData()
        a1.draw()

        pygame.display.flip()
        screen.fill((0,0,0))

    pygame.quit()

inp = input("which question do you want to see? 1,2,3,4,5,6 \n --")
if int(inp) == 1:
    q1()
elif int(inp) == 2:
    q2()
elif int(inp) == 3:
    q3()
elif int(inp) == 4:
    q4()
elif int(inp) == 5:
    q5()
elif int(inp) == 6:
    q6()
else:
    print("not an option")
