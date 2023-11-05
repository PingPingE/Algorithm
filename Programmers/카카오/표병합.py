'''
당신은 표 편집 프로그램을 작성하고 있습니다.
표의 크기는 50 × 50으로 고정되어있고 초기에 모든 셀은 비어 있습니다.
각 셀은 문자열 값을 가질 수 있고, 다른 셀과 병합될 수 있습니다.

위에서 r번째, 왼쪽에서 c번째 위치를 (r, c)라고 표현할 때, 당신은 다음 명령어들에 대한 기능을 구현하려고 합니다.

1. "UPDATE r c value"
- (r, c) 위치의 셀을 선택합니다.
- 선택한 셀의 값을 value로 바꿉니다.

2. "UPDATE value1 value2"
- value1을 값으로 가지고 있는 모든 셀을 선택합니다.
- 선택한 셀의 값을 value2로 바꿉니다.

3. "MERGE r1 c1 r2 c2"
- (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합합니다.
- 선택한 두 위치의 셀이 같은 셀일 경우 무시합니다.
- 선택한 두 셀은 서로 인접하지 않을 수도 있습니다. 이 경우 (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀만 영향을 받으며, 그 사이에 위치한 셀들은 영향을 받지 않습니다.
- 두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가지게 됩니다.
- 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀 값을 가지게 됩니다.
- 이후 (r1, c1) 와 (r2, c2) 중 어느 위치를 선택하여도 병합된 셀로 접근합니다.

4. "UNMERGE r c"
- (r, c) 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제합니다.
- 선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기의 상태로 돌아갑니다.
- 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가지게 됩니다.

5. "PRINT r c"
- (r, c) 위치의 셀을 선택하여 셀의 값을 출력합니다.
- 선택한 셀이 비어있을 경우 "EMPTY"를 출력합니다.
'''

def solution(commands):
    N = 51
    table = [[''] * N for _ in range(N)]
    links = {(r, c): (r, c) for r in range(N) for c in range(N)}

    def change_all_value_from(value_from, value_to):
        nonlocal table
        for r in range(N):
            for c in range(N):
                if table[r][c] == value_from:
                    table[r][c] = value_to

    def union(r1, c1, r2, c2):
        if (r1, c1) == (r2, c2):
            return
        print("Before: r1,c1:", links[(r1, c1)], "r2,c2:", links[(r2, c2)])
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)
        value = table[r1][c1] if (table[r1][c1] and table[r2][c2]) else table[r1][c1] + table[r2][c2]

        # 더 좌상단에 있는 셀에 값 몰아주기
        if r1 < r2 or (r1 == r2 and c1 < c2):
            table[r1][c1] = value
            table[r2][c2] = ''
            links[(r2, c2)] = (r1, c1)

        elif r1 > r2 or (r1 == r2 and c1 > c2):
            table[r2][c2] = value
            table[r1][c1] = ''
            links[(r1, c1)] = (r2, c2)

        # 모든 자식을 갱신 해줘야하는데 일일이 찾는 것 보다 그냥 다 갱신시키는게...
        for r_ in range(1, N):
            for c_ in range(1, N):
                find(r_, c_)
        print("After: r1,c1:", links[(r1, c1)], "r2,c2:", links[(r2, c2)])

    def find(r, c):
        if links[(r, c)] != (r, c):
            r_, c_ = links[(r, c)]
            links[(r, c)] = find(r_, c_)
        return links[(r, c)]

    def unmerge(target_r, target_c):
        root_r, root_c = find(target_r, target_c)
        value = table[root_r][root_c]
        print(f"Unmerge: ({target_r}, {target_c}): {value}, root:{(root_r, root_c)}")
        # (target_r,target_c)와 병합되었던 셀 모두 병합 해제
        for r in range(N):
            for c in range(N):
                r_, c_ = find(r, c)
                if (r_, c_) == (root_r, root_c):
                    links[(r, c)] = (r, c)
        # (target_r,target_c)에 value 위임
        table[root_r][root_c] = ''
        table[target_r][target_c] = value

    def execute_command(command_str):
        nonlocal table
        command = command_str.split()
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r, c, value = int(command[1]), int(command[2]), command[3]
                r, c = find(r, c)
                table[r][c] = value
            else:
                value_from, value_to = command[1], command[2]
                if value_from != value_to:
                    change_all_value_from(value_from, value_to)

        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            union(r1, c1, r2, c2)

        elif command[0] == 'UNMERGE':
            r, c = int(command[1]), int(command[2])
            unmerge(r, c)

        elif command[0] == 'PRINT':
            r, c = int(command[1]), int(command[2])
            r, c = find(r, c)
            if table[r][c]:
                return table[r][c]
            else:
                return "EMPTY"
        else:
            return

    answer = []
    for command in commands:
        ret = execute_command(command)
        if ret:
            answer.append(ret)
    return answer
