def time_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def int_to_time(t):
    h = t // 3600
    m = t % 3600 // 60
    s = t % 3600 % 60
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"


def solution(play_time, adv_time, logs):
    ans = [0, -1]  # 시작시간, 시청자 수
    play_time, adv_time = time_to_int(play_time), time_to_int(adv_time)
    #각 시간의 시청자 수
    arr = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start_t, end_t = time_to_int(start), time_to_int(end)
        for i in range(start_t, end_t):
            arr[i] += 1
        #누적 구할 때 빼주기 위해
        arr[end_t]-=1

    #각 시간까지의 누적 시청자 수
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]

    for ad_start in range(play_time-adv_time):
        tmp_ans=arr[ad_start+adv_time]-arr[ad_start-1]
        if tmp_ans > ans[1]:
            ans[0] = ad_start
            ans[1] = tmp_ans

    return int_to_time(ans[0])