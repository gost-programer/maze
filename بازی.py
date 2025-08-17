import turtle
import pygame
import sys
import pygame.locals as GAME_GLOBALS
import  pygame.event as GAME_EVENT

pygame.init()
playerVX = 0.099
playerVY = 0.098
color="red"
windowH=550
windowW=550
win=pygame.display.set_mode((windowW,windowH))
playerSize=20
playerX=0
playerY=450
leftDown = False
rightDown = False
upDown = False
downDown=False


def move():
    global playerX,playerY,playerVX,playerVY
    if leftDown:
        if playerVX >0:
            playerVX *=-1
        if playerX>0:
            playerX+=playerVX
    if rightDown:
        if playerVX <0:
            playerVX *=-1
        if playerX+playerSize<windowW:
            playerX+=playerVX
    if upDown:
        if playerVY > 0:
            playerVY *= -1
        if playerY>0:
            playerY+=playerVY
    if downDown:
        if playerVY < 0:
            playerVY *= -1
        if playerY+playerSize<windowH:
            playerY+=playerVY





while True :

    win.fill((0,0,0))
    mypick = pygame.image.load("'VFI.png.")
    win.blit(mypick, (playerX, playerY))
    pygame.draw.lines(win, (255, 250, 0), False, ((0, 0), (550, 0), (550, 450), (450, 450)), 10)
    pygame.draw.lines(win, (255, 250, 0), False, ((0, 0), (150, 0), (150, 50), (50, 50), (50, 100)), 10)
    pygame.draw.lines(win, (255, 250, 0), False,
    ((450, 500), (550, 500), (550, 550), (0, 550), (0, 500), (50, 500), (50, 500)), 10)
    pygame.draw.lines(win, (255, 250, 0), False,
    ((150, 100), (100, 100), (100, 200), (50, 200), (100, 200), (100, 300), (100, 200)
    , (100, 250), (150, 250), (150, 150), (200, 150), (200, 50), (250, 50), (200, 50), (200, 100),
    (300, 100), (300, 100), (300, 150)
    , (250, 150), (250, 250), (350, 250), (300, 250), (300, 300), (250, 300), (250, 350), (200, 350),
    (250, 350), (250, 400)
    , (300, 400), (300, 500)), 10)
    pygame.draw.lines(win, (255, 250, 0), False,
    ((250, 200), (200, 200), (200, 300), (150, 300), (150, 400), (200, 400), (200, 550)), 10)
    pygame.draw.line(win, (255, 250, 0), (0, 150), (50, 150), 10)
    pygame.draw.line(win, (255, 250, 0), (100, 550), (100, 500), 10)
    pygame.draw.lines(win, (255, 250, 0), False,
    ((0, 0), (0, 450), (50, 450), (50, 400), (50, 450), (150, 450), (150, 500)), 10)
    pygame.draw.lines(win, (255, 250, 0), False, ((0, 250), (50, 250), (50, 350), (100, 350), (100, 400)), 10)
    pygame.draw.lines(win, (255, 250, 0), False,
    ((400, 500), (400, 450), (350, 450), (400, 450), (400, 400), (500, 400), (400, 400)
    , (350, 400), (350, 350), (300, 350), (350, 350), (350, 300), (400, 300), (400, 150), (450, 150),
    (400, 150), (400, 200), (300, 200)
    , (350, 200), (350, 50), (400, 50), (400, 100), (500, 100), (500, 50), (500, 100), (500, 200),
    (450, 200), (450, 300), (500, 300)
    , (450, 300), (450, 350), (400, 350), (550, 350)), 10)
    pygame.draw.line(win, (255, 250, 0), (250, 550), (250, 450), 10)
    pygame.draw.line(win, (255, 250, 0), (350, 550), (350, 550), 10)
    pygame.draw.line(win, (255, 250, 0), (550, 350), (500, 350), 10)
    pygame.draw.line(win, (255, 250, 0), (450, 0), (450, 50), 10)
    pygame.draw.line(win, (255, 250, 0), (300, 0), (300, 50), 10)
    pygame.draw.line(win, (255, 250, 0), (500, 250), (550, 250), 10)
    pygame.draw.line(win, (255, 250, 0), (350, 550), (350, 500), 10)








    for event in GAME_EVENT.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                leftDown =True
            if event.key==pygame.K_RIGHT:
                rightDown=True
            if event.key == pygame.K_UP:
                upDown = True
            if event.key == pygame.K_DOWN:
                downDown =True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
            if event.key == pygame.K_RIGHT:
                rightDown = False
            if event.key == pygame.K_UP:
                upDown = False
            if event.key == pygame.K_DOWN:
                downDown = False

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    move()
    pygame.display.update()






