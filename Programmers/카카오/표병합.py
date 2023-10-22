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
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)
        value = table[r1][c1] if table[r1][c1] and table[r2][c2] else table[r1][c1] + table[r2][c2]
        if r1 < r2:
            table[r1][c1] = value
            table[r2][c2] = ''
            links[(r2, c2)] = (r1, c1)
        elif r1 > r2:
            table[r2][c2] = value
            table[r1][c1] = ''
            links[(r1, c1)] = (r2, c2)
        else:
            if c1 < c2:
                table[r1][c1] = value
                table[r2][c2] = ''
                links[(r2, c2)] = (r1, c1)
            else:
                table[r2][c2] = value
                table[r1][c1] = ''
                links[(r1, c1)] = (r2, c2)

    def find(r, c):
        if links[(r, c)] != (r, c):
            r_, c_ = links[(r, c)]
            links[(r, c)] = find(r_, c_)
        return links[(r, c)]

    def unmerge(r, c):
        target_r, target_c = r, c
        root_r, root_c = find(target_r, target_c)
        value = table[root_r][root_c]

        # 다른 병합된 셀도 있을 수 있으니
        for r in range(N):
            for c in range(N):
                r_, c_ = find(r, c)
                if (r_, c_) == (root_r, root_c):
                    links[(r, c)] = (r, c)

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

a = solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
print(a)