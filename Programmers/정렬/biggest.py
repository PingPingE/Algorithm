def swap(arr,i,j):
    arr[i], arr[j] = arr[j],arr[i]
def solution(numbers):
    answer = ''
    while len(numbers)>=2:
        for i in range(len(numbers)-1):
            s1 = str(numbers[i])
            s2 = str(numbers[i+1])

            if s1[0] > s2[0]:
                swap(numbers,i,i+1)
            elif s1[0] == s2[0]:
                n = min(len(s1),len(s2))
                if n <= 1:
                    if len(s2) == 1:
                        if s1[1] > s1[0]:
                            swap(numbers,i,i+1)
                            continue
                    elif len(s1) ==1 :
                        if s2[1] < s2[0]:
                            swap(numbers,i,i+1)
                            continue
                    continue
                else:
                    j= 1
                    k = 1
                    while j<len(s1) or k<len(s2):
                        if s1[j] > s2[k]:
                            swap(numbers,i,i+1)
                            break
                        elif s1[j] < s2[k]:
                            break
                        if j<len(s1)-1:
                            j += 1
                        if k < len(s2)-1:
                            k += 1

        answer += str(numbers[-1])
        del(numbers[-1])
    answer += str(numbers[0])
    return answer

numbers = [12,121]
print(solution(numbers))
