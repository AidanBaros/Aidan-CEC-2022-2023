from ast import In
from re import M
from turtle import pos
import pygame
import random

pygame.init()

class Port():
    def __init__(self, color, X, Y):
        self.color = color
        self.x = X
        self.y = Y
        self.width = 200
        self.height = 100

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Wire():
    def __init__(self, color, StartVal, EndVal):
        self.connected = False
        self.color = color
        self.Start = StartVal
        self.End = EndVal
        self.width = 20

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.Start, self.End, 20)

def collision(MousePos, i):
    if MousePos[0] >= i.x and MousePos[1] >= i.y and MousePos[0] <= (i.x + 200) and MousePos[1] <= (i.y + 100):
        return True
    return False

def win():
    for i in range(500):
        screen.fill((0,0,0))
        screen.blit(text, textRect)
        pygame.display.flip()
        
    return False


   
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenX,screenY = screen.get_size()
screen = pygame.display.set_mode((screenX,screenY))

ListofColors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
Ports = []
Wires = []
complete = []

running = True
edit = None
hovering = None
last = None

spacing = screenY//5

font = pygame.font.Font('freesansbold.ttf', 100)
text = font.render('You Win', True, (255,255,255))
textRect = text.get_rect()
textRect.center = (screenX // 2, screenY // 2)

random.shuffle(ListofColors)
for i in range(4):
    Ports.append(Port(ListofColors[i], 0, (spacing*(i+1)-25)))

random.shuffle(ListofColors)
for i in range(4):
    Ports.append(Port(ListofColors[i], screenX-200, (spacing*(i+1)-25)))



while running:
    MousePos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for i in Ports:
        if collision(MousePos,i):
            hovering = i
            break
    else:
        hovering = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_LCTRL]:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in Ports:
                if collision(MousePos, i) and i.color not in complete:
                    Wires.append(Wire(i.color, (i.x+100, i.y+50), MousePos))
                    edit = Wires[-1]
                    last = i
        if event.type == pygame.MOUSEBUTTONUP:
            if hovering == None and edit is not None:
                Wires.pop(-1)
            elif hovering != None and hovering.color != Wires[-1].color:
                Wires.pop(-1)
            elif hovering != None and hovering.color == Wires[-1].color and edit is not None and last != hovering:
                edit.End = (hovering.x + 100, hovering.y + 50)
                complete.append(edit.color)
            edit = None

    if edit is not None:
        edit.End = MousePos
    
    screen.fill((0,0,0))

    for i in Ports:
        i.draw(screen)
    for i in Wires:
        i.draw(screen)

    if hovering is not None:
        pygame.draw.rect(screen,(255,255,255),(hovering.x, hovering.y, hovering.width, hovering.height),5)

    if len(complete) == len(ListofColors):
        for i in range(len(ListofColors)):
            complete.sort()
            ListofColors.sort()
            if complete[i] == ListofColors[i]:
                running = win()

    pygame.display.flip()
pygame.quit()