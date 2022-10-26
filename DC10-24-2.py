import pygame
import random

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screenX, screenY = screen.get_size()


def Fibonacci(a, b, c, d, X, Y, check):
    xlist = [a, a - b, b * -1, 0]
    ylist = [d * -1, b * -1, 0, a]
    print(a, ", ", b)
    print(X, ", ", Y)
    print(c, ", ", d)

    pygame.draw.rect(
        screen,
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (
            X,
            Y,
            a,
            a,
        ),
    )

    X = X + (xlist[c])
    if c <= 0 and check == False:
        Y = Y
        check = True
        print("test")
    else:
        Y = Y + (ylist[c])
    print(X, ", ", Y)
    print()

    c += 1
    if c == len(xlist):
        c = 0
    return b, (a + b), c, a, X, Y, check


running = True

a = 0
b = 1
c = -1
d = 0
x = screenX // 2
y = screenY // 2
check = False

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_LCTRL]:
            running = False
        if keys[pygame.K_SPACE]:
            a, b, c, d, x, y, check = Fibonacci(a, b, c, d, x, y, check)
    pygame.display.flip()
pygame.quit()
