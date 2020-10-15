from collections import deque
import copy
def rotat(d):
    global board
    tmp = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp[j][2-i] = board[d][i][j]
    board[d] = copy.deepcopy(tmp)

def rotation(order): #시계방향
    global board
    dic = {'+': 1, '-': 3}
    for o in order:
        d,op = o[0],o[1] #면, + or -
        print("d,op", d,op)
        que = deque(maxlen=12)
        if d == 'U':
            que.append(board['B'][0])
            que.append([b[-1] for b in board['R']])
            que.append([board['F'][-1]])
            que.append([b[0] for b in board['L']])

            for _ in range(dic[op]):
                que.rotate(1)
            board['B'][0] = que[0][:]
            for e in range(3):
                board['R'][e][-1] = que[1][e]
                board['L'][e][0] =que[-1][e]
            board['F'][-1] = que[2][:]

        elif d == 'D':
            que.append(board['B'][-1])
            que.append([b[0] for b in board['R']])
            que.append([board['F'][0]])
            que.append([b[-1] for b in board['L']])

            for _ in range(dic[op]):
                que.rotate(1)
            board['B'][-1] = que[-1][:]
            for e in range(3):
                board['R'][e][0] = que[1][e]
                board['L'][e][-1] = que[-1][e]
            board['F'][0] = que[2][:]

        elif d == 'F':
            que.append(board['U'][0])
            que.append(board['R'][-1])
            que.append(board['D'][-1])
            que.append(board['L'][-1])

            for _ in range(dic[op]):
                que.rotate(1)

            board['U'][0] = que[0][:]
            board['R'][-1] = que[1][:]
            board['D'][-1] = que[2][:]
            board['L'][-1] = que[3][:]

        elif d == 'B':
            que.append(board['U'][-1])
            que.append(board['R'][0])
            que.append(board['D'][0])
            que.append(board['L'][0])

            for _ in range(dic[op]):
                que.rotate(1)

            board['U'][-1] = que[0][:]
            board['R'][0] = que[1][:]
            board['D'][0] = que[2][:]
            board['L'][0] = que[3][:]

        elif d == 'L':
            target = ['U','B','D','F']
            for t in target:
                que.append([b[0] for b in board[t]])

            for _ in range(dic[op]):
                que.rotate(1)

            for e,t in enumerate(target):
                for ee,val in enumerate(que[e]):
                    board[t][ee][0] = val

        else:  # R
            target = ['U', 'B', 'D', 'F']
            for t in target:
                que.append([b[-1] for b in board[target]])

            for _ in range(dic[op]):
                que.rotate(1)

            for e, t in enumerate(target):
                for ee, val in enumerate(que[e]):
                    board[t][ee][-1] = val
        #해당 면 rotation
        rotat(d)

T = int(input())
while T:
    board = {dir: [[color] * 3 for _ in range(3)] for dir, color in
             zip(['U', 'D', 'F', 'B', 'L', 'R'], ['w', 'y', 'r', 'o', 'g', 'b'])}
    T -= 1
    n = int(input())
    orders = list(input().split())
    rotation(orders)
    for p in board['U']:
        print(p)