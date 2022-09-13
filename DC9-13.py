import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,700))

class Apps():

    def __init__(self, XPos, YPos, ClickNum):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.XPos = XPos
        self.YPos = YPos
        self.ClickNum = ClickNum

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.XPos, self.YPos), 50)

appList = list()
for i in range(4):
    for j in range(3):
        appList.append(Apps((100*(j+1)),(100*(i+1)), 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            for i in appList:
                if ((i.XPos + 50 >= MousePos[0]) and (i.XPos -50 <= MousePos[0])) and ((i.YPos + 50 >= MousePos[1]) and (i.YPos -50 <= MousePos[1])):
                    i.ClickNum += 1
                    print(i.ClickNum)
    for i in appList:
        i.draw()

    appList.sort(key=lambda app: app.ClickNum)

    pygame.draw.circle(screen, appList[-1].color, (100,625),50)
    pygame.draw.circle(screen, appList[-2].color, (200,625),50)
    pygame.draw.circle(screen, appList[-3].color, (300,625),50)

    pygame.display.flip()
pygame.quit()