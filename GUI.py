import pygame, sys
from pygame.locals import *
black=pygame.Color(255,0,0,128)
spamRect = pygame.Rect(10, 20, 200, 300)
FPS = 30
WINDOWHEIGHT = 600
WINDOWWIDTH = 600
BOXSIZE = 50
GAPSIZE=10
ROWS=8
COLUMNS=8
BOARDWIDTH=BOXSIZE*COLUMNS+GAPSIZE*(COLUMNS-1)
BOARDHEIGHT=BOXSIZE*ROWS+GAPSIZE*(ROWS-1)
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH) / 2)
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT) / 2)
#print(XMARGIN,YMARGIN)
BLACK=(0,0,0,128)
GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)
BOARDCOLOR=GRAY
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
    return temp
def putpiece(player,y,x):
    if(player==1):
        pygame.draw.circle(StartWin,WHITE,drawpiece(y,x),int(BOXSIZE/2-1))
    else:
        pygame.draw.circle(StartWin,BLACK,drawpiece(y,x),int(BOXSIZE/2-1))
def drawboard():
    for i in range(COLUMNS):
        for j in range(ROWS):
            pygame.draw.rect(StartWin, CYAN, (XMARGIN+j*(BOXSIZE+GAPSIZE),YMARGIN+i*(BOXSIZE+GAPSIZE),BOXSIZE,BOXSIZE))
    pygame.draw.circle(StartWin,WHITE,drawpiece(3,3),int(BOXSIZE/2-1))
    pygame.draw.circle(StartWin,WHITE,drawpiece(4,4),int(BOXSIZE/2-1))
    pygame.draw.circle(StartWin,BLACK,drawpiece(4,3),int(BOXSIZE/2-1))
    pygame.draw.circle(StartWin,BLACK,drawpiece(3,4),int(BOXSIZE/2-1))
def drawpiece(y,x):
    t=(int(XMARGIN+x*(BOXSIZE+GAPSIZE)+BOXSIZE/2),int(YMARGIN+y*(BOXSIZE+GAPSIZE)+BOXSIZE/2))
    return t
def start():
    board[4][4]=1
    board[3][3]=1
    board[4][3]=2
    board[3][4]=2
def gameplay():
    global FPSClock,StartWin,n,total
    mouseClicked = False
    pygame.init()
    StartWin = pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH)) #DisplaySurface
    mousex = 0
    mousey = 0
    n=1
    flag=0
    now=2
    nob=2
    total=61
    chance=0
    #firstSelection = None # stores the (x, y) of the first box clicked.
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('OTHELLO', True,WHITE,BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WINDOWWIDTH/2,20)
    pygame.display.set_caption('Reversi')
    StartWin.fill(BLACK)
    drawboard()
    StartWin.blit(textSurfaceObj, textRectObj)
    while(True):
        for event in pygame.event.get():
            if(n%2):
                current=1
            else:
                current=2
            if(event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mx, my = event.pos
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
                if(n==total):
                    if(now>nob):
                        print("Player 2 wins.")
                    elif(nob>now):
                        print("Player 1 wins.")
                    else:
                        print("The match ends in a tie")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
board=[[0 for i in range(8)] for i in range(8)]
start()
gameplay()
