import datetime as dt
def to_datetime(target):
    end_str = " ".join(target.split(" ")[:-1])
    end = dt.datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S.%f")
    start = end - dt.timedelta(seconds=float(target.split(" ")[-1].split('s')[0])-0.001)
    return (start, end)
def solution(lines):
    answer = 0
    arr = []
    dic = {}
    for t_date in lines:
        arr.append(to_datetime(t_date))
        dic[arr[-1][0]] =0
        dic[arr[-1][1]] =0
    for a in arr:
        for k in dic:
            if a[0] > k+ dt.timedelta(seconds =0.999 )or a[1]<k:
                continue
            dic[k] += 1
    return max(dic.values())

'''
정확성  테스트
테스트 1 〉	통과 (1.97ms, 11.3MB)
테스트 2 〉	통과 (1230.43ms, 11.7MB)
테스트 3 〉	통과 (1146.66ms, 11.7MB)
테스트 4 〉	통과 (2.01ms, 11.3MB)
테스트 5 〉	통과 (15.56ms, 11.2MB)
테스트 6 〉	통과 (13.67ms, 11.3MB)
테스트 7 〉	통과 (1289.80ms, 11.8MB)
테스트 8 〉	통과 (1199.54ms, 11.7MB)
테스트 9 〉	통과 (13.79ms, 11.3MB)
테스트 10 〉	통과 (1.87ms, 11.4MB)
테스트 11 〉	통과 (1.82ms, 11.2MB)
테스트 12 〉	통과 (1197.88ms, 11.7MB)
테스트 13 〉	통과 (16.41ms, 11.3MB)
테스트 14 〉	통과 (1.76ms, 11.3MB)
테스트 15 〉	통과 (1.75ms, 11.3MB)
테스트 16 〉	통과 (1.74ms, 11.2MB)
테스트 17 〉	통과 (1.69ms, 11.2MB)
테스트 18 〉	통과 (3503.17ms, 12MB)
테스트 19 〉	통과 (4521.69ms, 12.1MB)
테스트 20 〉	통과 (4936.08ms, 12.1MB)
테스트 21 〉	통과 (1.71ms, 11.3MB)
테스트 22 〉	통과 (1.67ms, 11.3MB)
'''