#시도 중
def time_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_time(t):
    h = t // 3600
    m = t % 3600 // 60
    s = t % 3600 % 60
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"


def solution(play_time, adv_time, logs):
    play_time, adv_time = time_to_int(play_time), time_to_int(adv_time)

    # 각 시간의 시청자 수
    arr = [0 for _ in range(play_time + 2)]

    for log in logs:
        start, end = log.split('-')
        start_t, end_t = time_to_int(start), time_to_int(end)
        # 시청자 증가
        arr[start_t] += 1
        # 시청자 감소
        arr[end_t + 1] -= 1

    # 각 시간의 시청자 수
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    # 각 시간까지의 누적재생시간
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    ans = [0, arr[adv_time]]  # 시작시간, 누적재생시간

    for ad_start in range(1, len(arr)):
        ad_end = min(len(arr) - 1, ad_start + adv_time)
        tmp_ans = arr[ad_end] - arr[ad_start - 1]
        if tmp_ans > ans[1]:
            ans[0] = ad_start
            ans[1] = tmp_ans

    return int_to_time(ans[0])

'''
정확성  테스트
테스트 1 〉	통과 (1.93ms, 10.5MB)
테스트 2 〉	통과 (8.17ms, 10.7MB)
테스트 3 〉	통과 (16.89ms, 11.2MB)
테스트 4 〉	통과 (280.28ms, 27.9MB)
테스트 5 〉	통과 (491.87ms, 34.5MB)
테스트 6 〉	통과 (390.17ms, 22.8MB)
테스트 7 〉	실패 (541.43ms, 41MB)
테스트 8 〉	실패 (541.74ms, 45.8MB)
테스트 9 〉	통과 (804.18ms, 54.3MB)
테스트 10 〉	통과 (706.31ms, 54.6MB)
테스트 11 〉	실패 (725.93ms, 52.2MB)
테스트 12 〉	실패 (762.57ms, 49.7MB)
테스트 13 〉	통과 (751.49ms, 54.5MB)
테스트 14 〉	통과 (507.03ms, 40.9MB)
테스트 15 〉	통과 (74.99ms, 15.2MB)
테스트 16 〉	통과 (457.37ms, 40.8MB)
테스트 17 〉	통과 (955.02ms, 54.9MB)
테스트 18 〉	실패 (864.31ms, 42.2MB)
테스트 19 〉	통과 (4.36ms, 10.6MB)
테스트 20 〉	통과 (3.67ms, 10.5MB)
테스트 21 〉	통과 (136.50ms, 20.1MB)
테스트 22 〉	통과 (173.73ms, 20.2MB)
테스트 23 〉	통과 (691.96ms, 47.1MB)
테스트 24 〉	실패 (658.78ms, 40.9MB)
테스트 25 〉	통과 (211.06ms, 19.6MB)
테스트 26 〉	통과 (131.77ms, 15.1MB)
테스트 27 〉	통과 (131.36ms, 17.4MB)
테스트 28 〉	통과 (130.74ms, 16.9MB)
테스트 29 〉	통과 (128.21ms, 16.7MB)
테스트 30 〉	통과 (92.06ms, 14.2MB)
테스트 31 〉	통과 (106.04ms, 14.9MB)
'''