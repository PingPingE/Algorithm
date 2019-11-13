def solution(record):
    answer = []
    m = {}
    for i in range(len(record)):
        tmp = list(map(str, record[i].split()))
        #id mapping
        if tmp[1] not in m or (len(tmp) >2 and m[tmp[1]] != tmp[2]):
            m[tmp[1]] = tmp[2]
        if tmp[0] == 'Change':
            m[tmp[1]] = tmp[2]
        else:
            answer.append([tmp[0], tmp[1]])
    st = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    res = []
    for a in answer:
        res.append(str(m[a[1]]+st[a[0]]))
    return res