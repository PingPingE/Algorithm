'''
[문제]
"죠르디"의 동영상 재생시간 길이 play_time, 공익광고의 재생시간 길이 adv_time, 시청자들이 해당 동영상을 재생했던 구간 정보 logs가 매개변수로 주어질 때, 
시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려고 합니다. 이때, 공익광고가 들어갈 시작 시각을 구해서 return 하도록 solution 함수를 완성해주세요. 
만약, 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면, 그 중에서 가장 빠른 시작 시각을 return 하도록 합니다.

[제한사항]
play_time, adv_time은 길이 8로 고정된 문자열입니다.
play_time, adv_time은 HH:MM:SS 형식이며, 00:00:01 이상 99:59:59 이하입니다.
즉, 동영상 재생시간과 공익광고 재생시간은 00시간 00분 01초 이상 99시간 59분 59초 이하입니다.
공익광고 재생시간은 동영상 재생시간보다 짧거나 같게 주어집니다.
logs는 크기가 1 이상 300,000 이하인 문자열 배열입니다.

logs 배열의 각 원소는 시청자의 재생 구간을 나타냅니다.
logs 배열의 각 원소는 길이가 17로 고정된 문자열입니다.
logs 배열의 각 원소는 H1:M1:S1-H2:M2:S2 형식입니다.
H1:M1:S1은 동영상이 시작된 시각, H2:M2:S2는 동영상이 종료된 시각을 나타냅니다.
H1:M1:S1는 H2:M2:S2보다 1초 이상 이전 시각으로 주어집니다.
H1:M1:S1와 H2:M2:S2는 play_time 이내의 시각입니다.
시간을 나타내는 HH, H1, H2의 범위는 00~99, 분을 나타내는 MM, M1, M2의 범위는 00~59, 초를 나타내는 SS, S1, S2의 범위는 00~59까지 사용됩니다. 
잘못된 시각은 입력으로 주어지지 않습니다. (예: 04:60:24, 11:12:78, 123:12:45 등)

return 값의 형식

공익광고를 삽입할 시각을 HH:MM:SS 형식의 8자리 문자열로 반환합니다.
'''
def time_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_time(t):
    h = t // 3600
    m = t % 3600 // 60
    s = t % 3600 % 60
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"


def solution(play_time, adv_time, logs):
    #아래 로직에서는 adv_time을 -1해야함
    #ex) ad_start=1, adv_time=3인 경우, arr[1]~arr[4]을 보는데, 이건 3초가 아니라 4초 동안의 시청자 수를 보는 것임
    play_time, adv_time = time_to_int(play_time), time_to_int(adv_time) - 1

    # 각 시간의 시청자 수
    arr = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start_t, end_t = time_to_int(start), time_to_int(end)
        # 시청자 증가
        arr[start_t] += 1
        # 시청자 감소
        arr[end_t] -= 1

    # 각 시간의 시청자 수
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    # 각 시간까지의 누적재생시간
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    ans = [0, arr[adv_time]]  # 시작시간, 누적재생시간

    for ad_start in range(1, play_time - adv_time + 1):
        ad_end = ad_start + adv_time
        tmp_ans = arr[ad_end] - arr[ad_start - 1]
        if tmp_ans > ans[1]:
            ans[0] = ad_start
            ans[1] = tmp_ans

    return int_to_time(ans[0])

# print(solution("00:00:10", "00:00:03", ["00:00:00-00:00:03", "00:00:00-00:00:05", "00:00:03-00:00:05", "00:00:04-00:00:06"]))

'''
정확성  테스트
테스트 1 〉	통과 (1.45ms, 10.4MB)
테스트 2 〉	통과 (7.37ms, 10.5MB)
테스트 3 〉	통과 (15.36ms, 10.9MB)
테스트 4 〉	통과 (204.51ms, 27.9MB)
테스트 5 〉	통과 (280.18ms, 34.2MB)
테스트 6 〉	통과 (129.57ms, 21.5MB)
테스트 7 〉	통과 (438.79ms, 41MB)
테스트 8 〉	통과 (422.20ms, 45.9MB)
테스트 9 〉	통과 (530.14ms, 54.2MB)
테스트 10 〉	통과 (600.15ms, 54.6MB)
테스트 11 〉	통과 (592.26ms, 52.1MB)
테스트 12 〉	통과 (678.68ms, 49.6MB)
테스트 13 〉	통과 (623.54ms, 54.5MB)
테스트 14 〉	통과 (458.00ms, 40.8MB)
테스트 15 〉	통과 (49.56ms, 15.1MB)
테스트 16 〉	통과 (454.50ms, 40.9MB)
테스트 17 〉	통과 (617.56ms, 54.6MB)
테스트 18 〉	통과 (479.19ms, 42.1MB)
테스트 19 〉	통과 (1.63ms, 10.4MB)
테스트 20 〉	통과 (1.50ms, 10.4MB)
테스트 21 〉	통과 (135.37ms, 20.2MB)
테스트 22 〉	통과 (128.36ms, 20.2MB)
테스트 23 〉	통과 (530.55ms, 47MB)
테스트 24 〉	통과 (456.16ms, 40.9MB)
테스트 25 〉	통과 (103.67ms, 19.5MB)
테스트 26 〉	통과 (59.87ms, 14.8MB)
테스트 27 〉	통과 (69.87ms, 17.5MB)
테스트 28 〉	통과 (62.60ms, 17MB)
테스트 29 〉	통과 (58.94ms, 16.7MB)
테스트 30 〉	통과 (47.17ms, 14.1MB)
테스트 31 〉	통과 (49.24ms, 14.9MB)
'''
