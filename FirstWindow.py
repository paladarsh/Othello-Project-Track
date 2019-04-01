import pygame,sys
from pygame.locals import *
FPS = 30
WINDOWHEIGHT = 700
WINDOWWIDTH = 700
BLACK=(0,0,0,128)
GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0,128)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255,0,255,128)
CYAN = (0, 255, 255)
TAN=(210,180,140)

def SureToExit(kind):
    SureSurf=pygame.display.set_mode((700,300))
    SureImg=pygame.image.load('Sure.png')
    SureImg = pygame.transform.scale(SureImg, (700, 300))
    SureSurf.blit(SureImg,(0,0))
    SureObj = pygame.font.Font('calibri.ttf', 32)
    SureSurfaceObj = SureObj.render('Are you sure you want to quit?', True,WHITE,BLACK)
    SureRectObj = SureSurfaceObj.get_rect()
    SureRectObj.center = (WINDOWWIDTH/2,100)
    YesObj = pygame.font.Font('calibri.ttf', 32)
    YesSurfaceObj = YesObj.render('Yes', True,WHITE,BLACK)
    YesRectObj = YesSurfaceObj.get_rect()
    YesRectObj.center = (WINDOWWIDTH/2-100,200)
    NoObj = pygame.font.Font('calibri.ttf', 32)
    NoSurfaceObj = NoObj.render('No', True,WHITE,BLACK)
    NoRectObj = NoSurfaceObj.get_rect()
    NoRectObj.center = (WINDOWWIDTH/2+100,200)
    FirstWin.blit(SureSurfaceObj,SureRectObj)
    FirstWin.blit(YesSurfaceObj,YesRectObj)
    FirstWin.blit(NoSurfaceObj,NoRectObj)
    while(True):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                nx, ny = event.pos
                if(YesRectObj.collidepoint(nx,ny)):
                    pygame.quit()
                    sys.exit()
                if(NoRectObj.collidepoint(nx,ny)):
                    if(kind==1):
                        First()
                    elif(kind==2):
                        NextWin()
        pygame.display.update()
        
def NextWin():
    FirstWin=pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
    FirstWin.blit(OthelloImg,(0,0))
    VsCompImg=pygame.image.load('1 Player.png')
    VsCompRect=VsCompImg.get_rect()
    VsPlayerImg=pygame.image.load('2 Player.png')
    VsPlayerRect=VsPlayerImg.get_rect()
    VsCompRect.center=(WINDOWWIDTH/2,WINDOWHEIGHT/2-80)
    VsPlayerRect.center=(WINDOWWIDTH/2,WINDOWHEIGHT/2+180)
    FirstWin.blit(VsCompImg,VsCompRect)
    FirstWin.blit(VsPlayerImg,VsPlayerRect)
    while(True):
        for event in pygame.event.get():
            if(event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    SureToExit(2)
            elif event.type == MOUSEBUTTONUP:
                mox, moy = event.pos
                if(VsPlayerRect.collidepoint(mox,moy)):
                    import Gameplay
                elif(VsCompRect.collidepoint(mox,moy)):
                    import VsCompGUI
        pygame.display.update()
        FPSClock.tick(FPS)

def First():
    global FPSClock,FirstWin,OthelloImg
    pygame.font.init()
    FPSClock=pygame.time.Clock()
    FirstWin=pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
    OthelloImg=pygame.image.load('Othello.jpg')
    OthelloImg = pygame.transform.scale(OthelloImg, (700, 700))
    NewGameImg=pygame.image.load('Button.png')
    NewGameRect=NewGameImg.get_rect()
    NewGameObj = pygame.font.Font('calibri.ttf', 32)
    NewGameSurfaceObj = NewGameObj.render('New Game', True,BLACK,TAN)
    NewGameRectObj = NewGameSurfaceObj.get_rect()
    NewGameRectObj.center = (WINDOWWIDTH/2,300)
    ExitImg=pygame.image.load('Button.png')
    ExitRect=ExitImg.get_rect()
    ExitObj = pygame.font.Font('calibri.ttf', 32)
    ExitSurfaceObj = ExitObj.render('Exit', True,BLACK,TAN)
    ExitRectObj = ExitSurfaceObj.get_rect()
    ExitRectObj.center = (WINDOWWIDTH/2,400)
    pygame.init()
    pygame.display.set_caption('OTHELLO')
    FirstWin.fill(WHITE)
    NewGameRect.center=(WINDOWWIDTH/2,300)
    ExitRect.center=(WINDOWWIDTH/2,400)
    FirstWin.blit(OthelloImg,(0,0))
    FirstWin.blit(NewGameImg,NewGameRect)
    FirstWin.blit(ExitImg,ExitRect)
    FirstWin.blit(NewGameSurfaceObj,NewGameRectObj)
    FirstWin.blit(ExitSurfaceObj,ExitRectObj)
    while(True):
        for event in pygame.event.get():
            if(event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    SureToExit(1)
            elif event.type == MOUSEBUTTONUP:
                mx, my = event.pos
                if(NewGameRect.collidepoint(mx,my)):
                    FirstWin.blit(OthelloImg,(0,0))
                    NextWin()
                elif(ExitRect.collidepoint(mx,my)):
                    SureToExit(1)
        pygame.display.update()
        FPSClock.tick(FPS)
First()
