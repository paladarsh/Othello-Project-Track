import pygame, sys
from pygame.locals import *
FPS = 30
WINDOWHEIGHT = 700
WINDOWWIDTH = 700
BOXSIZE = 50
GAPSIZE=10
ROWS=8
COLUMNS=8
BOARDWIDTH=BOXSIZE*COLUMNS+GAPSIZE*(COLUMNS-1)
BOARDHEIGHT=BOXSIZE*ROWS+GAPSIZE*(ROWS-1)
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH) / 2)
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT) / 2)+100
BLACK=(0,0,0,128)
GRAY = (225, 225, 225)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255,128)
LIGHTORANGE=(255,160,122)
BOARDCOLOR=NAVYBLUE
BOXCOLOR=ORANGE
COLOR1=BLACK
COLOR2=WHITE
def highlight(x,y,prx,pry):
    #print(x,y)
    if(x!=prx or y!=pry):
        pygame.draw.rect(StartWin, BOARDCOLOR,(XMARGIN+prx*(BOXSIZE+GAPSIZE),YMARGIN+pry*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE), 4)
        pygame.draw.rect(StartWin, YELLOW,(XMARGIN+x*(BOXSIZE+GAPSIZE),YMARGIN+y*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE), 4)

def ispossible(player):
    for i in range(8):
        for j in range(8):
            if(issafe(j,i,player)):
               return True
    return False

def issafe(y,x,player):
    if (x>7 or y>7 or board[y][x]!=0):
        return False
    flag=False
    pos=-1
    #finding nearest position of same colour to the right
    for i in range(x+2,8):
        if(board[y][i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(x+1,pos):
            if(board[y][i]!=player%2+1):
                flag=False
                break
    if(flag==True):
        #print("Right")
        return True
    pos=-1
    #finding nearest position of same colour to the left
    for i in range(x-2,-1,-1):
        if(board[y][i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(pos+1,x):
            if(board[y][i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Left")
        return True
    pos=-1
    #finding nearest position of same colour to the bottom
    for i in range(y+2,8):
        if(board[i][x]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(y+1,pos):
            if(board[i][x]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Bottom")
        return True
    pos=-1
    #finding nearest position of same colour to the top
    for i in range(y-2,-1,-1):
        if(board[i][x]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(pos+1,y):
            if(board[i][x]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Top")
        return True
    pos=-1
    #finding nearest position of same colour on top right
    for i in range(2,9):
        if(x+i>7 or y-i<0):
            break
        if(board[y-i][x+i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(board[y-i][x+i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Top Right")
        return True
    pos=-1
    #finding nearest position of same colour on top left
    for i in range(2,9):
        if(x-i<0 or y-i<0):
            break
        if(board[y-i][x-i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(board[y-i][x-i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Top Left")
        return True
    pos=-1
    #finding nearest position of same colour on bottom right
    for i in range(2,9):
        if(x+i>7 or y+i>7):
            break
        if(board[y+i][x+i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(board[y+i][x+i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Bottom Right")
        return True
    pos=-1
    #finding nearest position of same colour on bottom left
    for i in range(2,9):
        if(x-i<0 or y+i>7):
            break
        if(board[y+i][x-i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(board[y+i][x-i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Bottom Left")
        return True
    return False

def change(y,x,player):
    flag=False
    pos=-1
    boards=[[0 for i in range(8)]for i in range(8)]
    for i in range(8):
        for j in range(8):
            boards[i][j]=board[i][j]
    #changing nearest position of same colour to the right
    for i in range(x+2,8):
        if(boards[y][i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(x+1,pos):
            if(boards[y][i]!=player%2+1):
                flag=False
                break
    if(flag==True):
        for i in range(x+1,pos):
            board[y][i]=player
            putpiece(player,y,i)
    flag=False
    pos=-1
    #changing nearest position of same colour to the left
    for i in range(x-2,-1,-1):
        if(boards[y][i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(pos+1,x):
            if(boards[y][i]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(pos+1,x):
            board[y][i]=player
            putpiece(player,y,i)
    flag=False
    pos=-1
    #changing nearest position of same colour to the bottom
    for i in range(y+2,8):
        if(boards[i][x]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(y+1,pos):
            if(boards[i][x]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(y+1,pos):
            board[i][x]=player
            putpiece(player,i,x)
    flag=False
    pos=-1
    #changing nearest position of same colour to the top
    for i in range(y-2,-1,-1):
        if(boards[i][x]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(pos+1,y):
            if(boards[i][x]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(pos+1,y):
            board[i][x]=player
            putpiece(player,i,x)
    flag=False
    pos=-1
    #changing nearest position of same colour on top right
    for i in range(2,9):
        if(x+i>7 or y-i<0):
            break
        if(boards[y-i][x+i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(boards[y-i][x+i]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(1,pos):
            board[y-i][x+i]=player
            putpiece(player,y-i,x+i)
    flag=False
    pos=-1
    #changing nearest position of same colour on top left
    for i in range(2,9):
        if(x-i<0 or y-i<0):
            break
        if(boards[y-i][x-i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(boards[y-i][x-i]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(1,pos):
            board[y-i][x-i]=player
            putpiece(player,y-i,x-i)
    flag=False
    pos=-1
    #changing nearest position of same colour on bottom right
    for i in range(2,9):
        if(x+i>7 or y+i>7):
            break
        if(boards[y+i][x+i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(boards[y+i][x+i]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(1,pos):
            board[y+i][x+i]=player
            putpiece(player,y+i,x+i)
    flag=False
    pos=-1
    #changing nearest position of same colour on bottom left
    for i in range(2,9):
        if(x-i<0 or y+i>7):
            break
        if(boards[y+i][x-i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(boards[y+i][x-i]!=player%2+1):
                flag=False
    if(flag==True):
        for i in range(1,pos):
            board[y+i][x-i]=player
            putpiece(player,y+i,x-i)

def find(player):
    c=0
    for i in range(8):
        for j in range(8):
            if(board[i][j]==player):
                c+=1
    return c

def pixelstocoordinates(xx,yy):
    xp=(xx-int(XMARGIN))//int(BOXSIZE+GAPSIZE)
    yp=(yy-int(YMARGIN))//int(BOXSIZE+GAPSIZE)
    temp=(xp,yp)
    #print(xx,yy)
    return temp

def putpiece(player,y,x):
    if(player==1):
        pygame.draw.circle(StartWin,COLOR1,drawpiece(y,x),int(BOXSIZE/2-3))
    else:
        pygame.draw.circle(StartWin,COLOR2,drawpiece(y,x),int(BOXSIZE/2-3))

def drawboard():
    for i in range(COLUMNS):
        for j in range(ROWS):
            pygame.draw.rect(StartWin, BOXCOLOR, (XMARGIN+j*(BOXSIZE+GAPSIZE),YMARGIN+i*(BOXSIZE+GAPSIZE),BOXSIZE,BOXSIZE))
            
    pygame.draw.circle(StartWin,COLOR2,drawpiece(3,4),int(BOXSIZE/2-3))
    pygame.draw.circle(StartWin,COLOR2,drawpiece(4,3),int(BOXSIZE/2-3))
    pygame.draw.circle(StartWin,COLOR1,drawpiece(4,4),int(BOXSIZE/2-3))
    pygame.draw.circle(StartWin,COLOR1,drawpiece(3,3),int(BOXSIZE/2-3))

def drawpiece(y,x):
    t=(int(XMARGIN+x*(BOXSIZE+GAPSIZE)+BOXSIZE/2),int(YMARGIN+y*(BOXSIZE+GAPSIZE)+BOXSIZE/2))
    return t

def start():
    board[4][4]=1
    board[3][3]=1
    board[4][3]=2
    board[3][4]=2
    
def win(now,nob):
    gameover=True
    if(now>nob):
        toprint="Player 2 wins."
    elif(nob>now):
        toprint="Player 1 wins."
    else:
        toprint="The match ends in a tie"
    FinalObj = pygame.font.Font('calibri.ttf', 70)
    FinalSurfaceObj = FinalObj.render(toprint, True,BLACK,WHITE)
    FinalRectObj = FinalSurfaceObj.get_rect()
    FinalRectObj.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
    StartWin.blit(FinalSurfaceObj,FinalRectObj)
def gameplay():
    global FPSClock,StartWin,n,total,gameover
    FPSCLOCK=pygame.time.Clock()
    pygame.init()
    BackImg=pygame.image.load('Background.jpg')
    BackImg = pygame.transform.scale(BackImg, (700, 700))
    StartWin=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    ScoreImg=pygame.image.load('Scoreboard.png')
    ScoreImg = pygame.transform.scale(ScoreImg,(350,150))
    ScoreRect=ScoreImg.get_rect()
    ScoreRect.center=((WINDOWWIDTH/2,75))
    mousex=0
    gameover=False
    mousey=0
    n=1
    now=2
    nob=2
    px=0
    py=0
    total=61
    StartWin.blit(BackImg,(0,0))
    pygame.draw.rect(StartWin,BOARDCOLOR,(XMARGIN-GAPSIZE,YMARGIN-GAPSIZE,BOXSIZE*COLUMNS+GAPSIZE*(ROWS+1),BOXSIZE*ROWS+GAPSIZE*(COLUMNS+1)))
    drawboard()
    StartWin.blit(ScoreImg,ScoreRect)
    pygame.draw.circle(StartWin,COLOR1,(int(WINDOWWIDTH/2-75),65),int(BOXSIZE/2-3))
    pygame.draw.circle(StartWin,COLOR2,(int(WINDOWWIDTH/2+75),65),int(BOXSIZE/2-3))
    BlackObj = pygame.font.Font('calibri.ttf', 40)
    BlackSurfaceObj = BlackObj.render(str(nob), True,BLACK,WHITE)
    BlackRectObj = BlackSurfaceObj.get_rect()
    BlackRectObj.center = (WINDOWWIDTH/2-75,110)
    WhiteObj = pygame.font.Font('calibri.ttf', 40)
    WhiteSurfaceObj = WhiteObj.render(str(now), True,WHITE,GRAY)
    WhiteRectObj = WhiteSurfaceObj.get_rect()
    WhiteRectObj.center = (WINDOWWIDTH/2+75,110)
    TurnObj = pygame.font.Font('calibri.ttf', 40)
    TurnSurfaceObj = TurnObj.render('Player 1\'s turn', True,BLACK,WHITE)
    TurnRectObj = TurnSurfaceObj.get_rect()
    TurnRectObj.center = (WINDOWWIDTH/2,175)
    StartWin.blit(BlackSurfaceObj,BlackRectObj)
    StartWin.blit(WhiteSurfaceObj,WhiteRectObj)
    StartWin.blit(TurnSurfaceObj,TurnRectObj)
    while(True):
        for event in pygame.event.get():
            if(n%2):
                current=1
            else:
                current=2
            pr='Player '+str(current%2+1)+'\'s turn'
            TurnObj = pygame.font.Font('calibri.ttf', 40)
            TurnSurfaceObj = TurnObj.render(pr, True,BLACK,WHITE)
            TurnRectObj = TurnSurfaceObj.get_rect()
            TurnRectObj.center = (WINDOWWIDTH/2,175)
            if(event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mx, my = event.pos
                if(mousex>=0 and mousey>=0 and mousex<8 and mousey<8):
                    px,py=mousex,mousey
                mousex,mousey=pixelstocoordinates(mx,my)
                if(mousex>=0 and mousey>=0 and mousex<8 and mousey<8 and not gameover):
                    highlight(mousex,mousey,px,py)
            elif event.type == MOUSEBUTTONUP:
                mx, my = event.pos
                mousex,mousey=pixelstocoordinates(mx,my)
                if(not(ispossible(current))):
                    total+=1
                    n+=1
                    continue
                if(issafe(mousey,mousex,current)):
                    board[mousey][mousex]=current
                    n+=1
                    change(mousey,mousex,current)
                    putpiece(current,mousey,mousex)
                    nob=find(1)
                    now=find(2)
                    BlackObj = pygame.font.Font('calibri.ttf', 40)
                    BlackSurfaceObj = BlackObj.render(str(nob), True,BLACK,WHITE)
                    BlackRectObj = BlackSurfaceObj.get_rect()
                    BlackRectObj.center = (WINDOWWIDTH/2-75,110)
                    WhiteObj = pygame.font.Font('calibri.ttf', 40)
                    WhiteSurfaceObj = WhiteObj.render(str(now), True,WHITE,GRAY)
                    WhiteRectObj = WhiteSurfaceObj.get_rect()
                    WhiteRectObj.center = (WINDOWWIDTH/2+75,110)
                    StartWin.blit(ScoreImg,ScoreRect)
                    pygame.draw.circle(StartWin,COLOR1,(int(WINDOWWIDTH/2-75),65),int(BOXSIZE/2-3))
                    pygame.draw.circle(StartWin,COLOR2,(int(WINDOWWIDTH/2+75),65),int(BOXSIZE/2-3))
                    StartWin.blit(BlackSurfaceObj,BlackRectObj)
                    StartWin.blit(WhiteSurfaceObj,WhiteRectObj)
                    StartWin.blit(TurnSurfaceObj,TurnRectObj)
                if(n==total):
                    win(now,nob)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
board=[[0 for i in range(8)] for i in range(8)]
start()
gameplay()
