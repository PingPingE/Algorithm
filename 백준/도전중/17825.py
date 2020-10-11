from collections import deque
turn = list(map(int, input().split()))
red = [[i for i in range(j,j+2*5,2)] for j in range(2,41,10)]
blue = {10: [13,16,19,25], 20:[22,24,25], 30:[28,27,26,25], 25:[30,35,40]}
que= deque()
print(red)
#-1,-1은 시작칸, -2,-2는 도착칸
que.extend([[0]+[[[-1,-1] for _ in range(4)]]+[0]]) #[현재 점수, 각 말의 현재위치(r,c), 현재 turn]
# 현재 위치->(r,c):red 위면 r이 최대 3, c가 최대 4일테고, blue 위면 r은 10이상, c는 해당 key의 value len미만
#r이 25이고 c가 2초과면 도착 or red에서 끝까지 이상가면 도착
ret= 0
print(que[0])
while que:
    cur_point, horses ,count= que.popleft()
    if count >=10:
        print("end:",cur_point, horses, count)
        ret = max(ret, cur_point)
        continue
    print("======================")
    print(cur_point, horses, count)
    for e,horse in enumerate(horses):
        r,c = horse
        print("start: ",r,c)
        stat= 0
        if r>-2: #도착칸이 아니면
            nr = r
            if r==-1:
                nr = 0
            nc = c
            n_point = 0
            if nr in blue:
                print("blue---")
                num = (nc+turn[count])//len(blue[nr])
                remain = (nc+turn[count])%len(blue[nr])
                if num>0:
                    if nr ==25 or remain >= len(blue[25]):
                        nr,nc=-2,-2
                    else:
                        nr = 25

                if nr != -2:
                    nc = remain
                    n_point = blue[nr][nc]

                print("nr,nc,n_point",nr,nc,n_point)
            else:
                stat =1
                print("red---")
                num = (nc+turn[count])//5
                nr += num
                nc = (nc+turn[count])%5
                if nr>=4:
                    nr,nc =-2,-2
                else:
                    n_point = red[nr][nc]

            if stat and n_point in blue:
                nr = n_point
                nc = -1

            if nr!= -2 and [nr, nc] in horses:#이미 다른 horse가 있다면
                continue

            print("step:", turn[count], "move to:", nr, nc, "is empty?", horses)
            horses[e] = [nr, nc]
            print("push: ",[cur_point + n_point, list(h[:] for h in horses), count + 1])
            que.append([cur_point + n_point, list(h[:] for h in horses), count + 1])
            horses[e] = [r,c]
            if count ==0: #첫 시작은 한마리만 하면 됨
                break
print(ret)