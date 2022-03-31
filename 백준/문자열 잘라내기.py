'''
문제)
R개의 행과 C개의 열로 이루어진 테이블이 입력으로 주어진다. 이 테이블의 원소는 알파벳 소문자이다.

각 테이블의 열을 위에서 아래로 읽어서 하나의 문자열을 만들 수 있다. 예제 입력에서

dobarz
adatak
이 주어지는 경우 "da", "od", "ba", "at", "ra", "zk"와 같이 6개의 문자열들이 만들어지게 된다.

만약 가장 위의 행을 지워도 테이블의 열을 읽어서 문자열이 중복되지 않는다면, 가장 위의 행을 지워주고, count의 개수를 1 증가시키는, 이 과정을 반복한다.
만약 동일한 문자열이 발견되는 경우, 반복을 멈추고 count의 개수를 출력 후 프로그램을 종료한다.

테이블이 주어질 경우 count의 값을 구해보자.

입력)
첫 번째 줄에는 테이블의 행의 개수와 열의 개수인 R과 C가 주어진다. (2 ≤ R, C ≤ 1000)

이후 R줄에 걸쳐서 C개의 알파벳 소문자가 주어진다. 가장 처음에 주어지는 테이블에는 열을 읽어서 문자열을 만들 때, 동일한 문자열이 존재하지 않는 입력만 주어진다.

출력)
문제의 설명과 같이 count의 값을 출력한다.

'''
#227552kb	652ms
import sys
R,C = map(int, input().split())
arr = list('' for _ in range(C))
for r in range(R):
    row = list(sys.stdin.readline().strip())
    for c in range(C):
        arr[c] = row[c] + arr[c]

count = 0
while True:
    tmp_set = set(arr)
    if len(tmp_set) < C:
        break
    count+=1
    arr = list(map(lambda x: x[:-1], arr))
print(count-1 if count >=1 else 0)



#============삽질 기록
#왜 두개만 보냐
import sys
R,C = map(int, input().split())
arr=[[],[]]
flag = 0
count = 0
isbreak = 0
for _ in range(R):
    if not arr[not flag] or isbreak:
        arr[flag] = list(sys.stdin.readline().strip())
        flag = not flag
        continue

    str_sets = set()
    arr[flag] = list(sys.stdin.readline().strip())
    # print(arr)
    for c in range(C):
        tmp = arr[not flag][c]+arr[flag][c]
        if tmp in str_sets:
            isbreak = 1
            break
        str_sets.add(tmp)

    if not isbreak:
        count += 1
        flag = not flag

print(count)

