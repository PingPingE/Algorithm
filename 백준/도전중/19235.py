N = int(input())
order = [tuple(map(int, input().split())) for _ in range(N)] #t,x,y -> 블록 t를 (x,y) / (x,y),(x,y+1) / (x,y),(x+1, y)에 놓은 경우
#t=1: 1*1, t=2: 1*2, t=3: 2*1 -> 블록크기
board = [[0 for _ in range(10)] for __ in range(10)]
point = 0
def move(color, from_=9, stat=0): #color: 0은 blue, 1은 green
    global board
    print("move:",color, from_,stat)
    for b in board:
        print(b)
    if color == 0: #blue
        for k in range(4):
            board[k][from_] = 0
        for i in range(9, 3,-1):#열
            for j in range(4):
                if board[j][i] == 1: continue
                if i-1 >3:
                    x =i-1
                    if stat:
                        while x>3 and board[j][x] ==0:
                            if x-1>3:
                                x-=1
                            else:
                                break
                    board[j][i] = board[j][x]
                    board[j][x] = 0

    else:#green
        board[from_][:] = [0 for _ in range(10)]
        for i in range(9, 3,-1):#행
            for j in range(4):
                if board[i][j] == 1: continue
                if i-1 >3:
                    x=i-1
                    if stat:
                        while x>3 and board[x][j] == 0:
                            if x-1>3:
                                x-=1
                            else:
                                break

                    board[i][j] = board[x][j]
                    board[x][j]=0

    print("===after===")
    for b in board:
        print(b)
def isFull():#행과 열이 가득한 경우 check
    global point
    #blue
    while True:
        for i in range(9,3,-1):
            for j in range(4):
                if board[j][i] == 0:
                    break
            else:
                move(0,i,1)
                point+=1
                break
        else:
            break
    #green
    while True:
        for i in range(9,3,-1):
            if sum(board[i][:]) == 4:
                move(1,i,1)
                point +=1
                break
        else:
            break

def special_check():#투명한 칸 체크 + 있으면 이동
    #blue
    while True:
        stat= 0
        for i in [4,5]:
            for j in range(4):
                if board[j][i]== 1:
                    stat = 1
                    break
            if stat:
                break
        if stat:
            move(0)
        else:
            break
    #green
    while True:
        if sum(board[4][:]) + sum(board[5][:]) == 0: break
        move(1)

def set_block(type, r,c): #놓고 move
    global board
    br, bc = r, 4
    gr, gc = 4, c
    if type == 1:
        #blue
        while bc<9 and board[br][bc+1] ==0:
            bc+=1
        board[br][bc] = 1

        #green
        while gr < 9 and board[gr+1][gc] == 0:
            gr += 1
        board[gr][gc] = 1

    elif type==2:
        # blue
        while bc<8 and board[br][bc+1]+board[br][bc+2] == 0:
            bc+=1
        board[br][bc] = 1
        board[br][bc+1] = 1
        # green
        while gr<9 and board[gr+1][gc]+board[gr+1][gc+1] == 0:
            gr+=1
        board[gr][gc] = 1
        board[gr][gc+1] = 1

    else:
        # blue
        while bc<9 and board[br][bc+1]+board[br+1][bc+1] == 0:
            bc+=1
        board[br][bc] = 1
        board[br+1][bc] = 1
        # green
        while gr<8 and board[gr+1][gc] + board[gr+2][gc] == 0:
            gr+=1
        board[gr][gc] = 1
        board[gr+1][gc] =1

    isFull()
    special_check()


def get_count():
    count = 0
    for i in range(10):
        count += sum(board[i][:])
    return count

for o in order:
    print("order:",o)
    set_block(o[0],o[1],o[2])
isFull()
special_check()
print(point)
print(get_count())