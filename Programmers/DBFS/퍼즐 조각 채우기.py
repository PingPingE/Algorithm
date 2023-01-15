# 블럭 추출하고 -> 회전 시킨 위치도 추출 -> 상대 위치로 조절 -> game board에 대입 -> 맞는거 있으면 counting

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
# table 자체를 돌려버리고?
def rotation_clockwise_90(table):
    N = len(table)
    ret_table = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret_table[j][N - 1 - i] = table[i][j]
    return ret_table

#회전시킨 상태에서의 좌표값 받기
def get_area_info(table, keys):
    N = len(table)
    tmp_info = {i: [] for i in keys}
    for r in range(N):
        for c in range(N):
            if table[r][c] > 1:
                tmp_info[table[r][c]].append((r, c))

    #상대 위치로 값 조절
    for k in tmp_info:
        min_y, min_x = N,N
        for y,x in tmp_info[k]:
            min_y , min_x = min(min_y, y), min(min_x, x)
        tmp_info[k] = [(y-min_y, x-min_x) for y,x in tmp_info[k]]
    return tmp_info

#초기 상태에서의 영역 나누기 + 좌표값 추출
def extract_block(table, target_n=1):
    info_dict = {}
    N = len(table)
    num = 2
    for r in range(N):
        for c in range(N):
            if table[r][c] == target_n:
                st = [(r, c)]
                table[r][c] = num
                info_list = [(r, c)]
                min_y,min_x= r,c
                while st:
                    y, x = st.pop()
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and table[ny][nx] == target_n:
                            min_y,min_x = min(min_y,ny), min(min_x,nx)
                            table[ny][nx] = num
                            st.append((ny, nx))
                            info_list.append((ny, nx))
                info_dict[num] =[[(y-min_y, x-min_x) for y,x in info_list]]
                num += 1

    # for t in table:
    #     print(t)

    return info_dict

def solution(game_board, table):
    answer = 0
    #초기 모양 추출
    block_dict = extract_block(table)

    #회전시킨 모양 추출
    for _ in range(3):
        table = rotation_clockwise_90(table)
        tmp_info = get_area_info(table, block_dict)
        for k, v in tmp_info.items():
            block_dict[k].append(v)

    #game_board에서의 빈칸 영역 구하기
    table_dict = extract_block(game_board,0)

    #이미 맞춘 블럭은 빼줘야해서 필요
    done = set()
    for k1,v1 in table_dict.items():
        target_block = set(v1[0])
        flag= 0

        #한 블럭씩 대입
        for k2,v2 in block_dict.items():
            if k2 in done: continue
            for block in v2:
                if target_block == set(block):
                    # print(k1, ': ', target_block)
                    answer += len(block)
                    done.add(k2)
                    flag=1
                    break
            if flag: break
    return answer

t1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
t2 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(t1,t2))
