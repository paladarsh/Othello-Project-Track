def printf():
    print("  0 1 2 3 4 5 6 7")
    for i in range(8):
        print(i,end=' ')
        for j in range(8):
            print(board[i][j],end=' ')
        print()
def ispossible(player):
    for i in range(8):
        for j in range(8):
            if(issafe(j,i,player,board)):
               return True
    return False
def copy(froms):
    to=[[0 for i in range(8)]for i in range(8)]
    for i in range(8):
        for j in range(8):
            to[i][j]=froms[i][j]
    return to
def issafe(y,x,player,givenboard):
    if (x>7 or y>7 or givenboard[y][x]!=0):
        return False
    flag=False
    pos=-1
    #finding nearest position of same colour to the right
    for i in range(x+2,8):
        if(givenboard[y][i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(x+1,pos):
            if(givenboard[y][i]!=player%2+1):
                flag=False
                break
    if(flag==True):
        #print("Right")
        return True
    pos=-1
    #finding nearest position of same colour to the left
    for i in range(x-2,-1,-1):
        if(givenboard[y][i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(pos+1,x):
            if(givenboard[y][i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Left")
        return True
    pos=-1
    #finding nearest position of same colour to the bottom
    for i in range(y+2,8):
        if(givenboard[i][x]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(y+1,pos):
            if(givenboard[i][x]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Bottom")
        return True
    pos=-1
    #finding nearest position of same colour to the top
    for i in range(y-2,-1,-1):
        if(givenboard[i][x]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(pos+1,y):
            if(givenboard[i][x]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Top")
        return True
    pos=-1
    #finding nearest position of same colour on top right
    for i in range(2,9):
        if(x+i>7 or y-i<0):
            break
        if(givenboard[y-i][x+i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(givenboard[y-i][x+i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Top Right")
        return True
    pos=-1
    #ging nearest position of same colour on top left
    for i in range(2,9):
        if(x-i<0 or y-i<0):
            break
        if(givenboard[y-i][x-i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(givenboard[y-i][x-i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Top Left")
        return True
    pos=-1
    #finding nearest position of same colour on bottom right
    for i in range(2,9):
        if(x+i>7 or y+i>7):
            break
        if(givenboard[y+i][x+i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(givenboard[y+i][x+i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Bottom Right")
        return True
    pos=-1
    #finding nearest position of same colour on bottom left
    for i in range(2,9):
        if(x-i<0 or y+i>7):
            break
        if(givenboard[y+i][x-i]==player):
            pos=i
            break
    if(pos!=-1):
        flag=True
        for i in range(1,pos):
            if(givenboard[y+i][x-i]!=player%2+1):
                flag=False
    if(flag==True):
        #print("Bottom Left")
        return True
    return False
def think():
    boards=copy(board)
    (values,y,x)=rec(boards,2,1)
    return (y,x)
def rec(presboard,player,depth):
    if(depth==2):
        bestval=-64
        (besty,bestx)=(-2,-2)
        forthisrec=copy(presboard)
        #Computer's chance
        for i in range(8):
            for j in range(8):
                if(issafe(i,j,2,forthisrec)):
                        change(i,j,2,forthisrec)
                        value=find(2,forthisrec)-find(1,forthisrec)
                        if(value>bestval):
                            bestval=value
                            (besty,bestx)=(i,j)
                            forthisrec=copy(presboard)
        return (bestval,besty,bestx)
    else:
        if(player==1):
            bestval=64
            (besty,bestx)=(-2,-2)
            rety,retx=0,0
            forthisrec=copy(presboard)
            for i in range(8):
                for j in range(8):
                    if(issafe(i,j,1,forthisrec)):
                            change(i,j,1,forthisrec)
                            (value,rety,retx)=rec(forthisrec,2,depth+1)
                            if(value<bestval):
                                bestval=value
                                (besty,bestx)=(i,j)
                            forthisrec=copy(presboard)
            return (bestval,besty,bestx)
        if(player==2):
            bestval=-64
            (besty,bestx)=(-2,-2)
            rety,retx=0,0
            forthisrec=copy(presboard)
            for i in range(8):
                for j in range(8):
                    if(issafe(i,j,2,forthisrec)):
                            change(i,j,2,forthisrec)
                            (value,rety,retx)=rec(forthisrec,1,depth)
                            if(value>bestval):
                                bestval=value
                                (besty,bestx)=(i,j)
                            forthisrec=copy(presboard)
            return (bestval,besty,bestx)
def start():
    board[4][4]=1
    board[3][3]=1
    board[4][3]=2
    board[3][4]=2
    printf()
    gameplay()
def change(y,x,player,boards):
    #changing nearest position of same colour to the right
    flag=False
    pos=-1
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
            boards[y][i]=player
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
            boards[y][i]=player
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
            boards[i][x]=player
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
            boards[i][x]=player
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
            boards[y-i][x+i]=player
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
            boards[y-i][x-i]=player
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
            boards[y+i][x+i]=player
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
            boards[y+i][x-i]=player
def find(player,thisboard):
    c=0
    for i in range(8):
        for j in range(8):
            if(thisboard[i][j]==player):
                c+=1
    return c
def gameplay():
    n=1
    now=2
    nob=2
    total=61
    while(n!=total):
        if(n%2):
            if(not(ispossible(1))):
                input("No valid moves. Press any key to pass.")
                total+=1
                n+=1
                continue
            m=(input("Player 1, Enter the position to be filled:"))            
            a=int(m[0])
            b=int(m[1])
            if(issafe(a,b,1,board)):
                board[a][b]=1
                n+=1
                change(a,b,1,board)
                printf()
                nob=find(1,board)
                now=find(2,board)
                print("Score:\nWhites=",now," ; Blacks=",nob)
            else:
                print("Please try again!")
        else:
            if(not(ispossible(2))):
                input("No valid moves. Press any key to pass.")
                total+=1
                n+=1
                continue
            print("Computer is Thinking....")
            (a,b)=think()
            board[a][b]=2
            n+=1
            change(a,b,2,board)
            printf()
            now=find(2,board)
            nob=find(1,board)
            print("Score:\nWhites=",now," ; Blacks=",nob)
    if(now>nob):
        print("Player 2 wins.")
    elif(nob>now):
        print("Player 1 wins.")
    else:
        print("The match ends in a tie")
board=[[0 for i in range(8)] for i in range(8)]
start()
