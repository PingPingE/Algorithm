A = list(map(int, input().split())) #크기 n, 범위는 [0,k]
B = [0 for _ in range(len(A)+1)] #n+1만큼
C = [0 for _ in range(max(A)+1)] #k+1만큼

for a in A: #각 원소 count
    C[a] += 1

for ind in range(1,len(C)): #누적합 구하기(즉, C[ind]는 ind보다 작거나 같은 값의 개수를 나타냄)
    C[ind] = C[ind] + C[ind-1]

for i in range(len(A)-1, -1,-1): #뒤에서 부터 넣어주기(자기보다 작거나 같은 값의 개수를 알고있으므로) => stable하다
    B[C[A[i]]] = A[i]
    C[A[i]] -= 1

print("Before: ",A)
print("After: ",B[1:])

'''
Test1)
3 1 5 62 3
Before:  [3, 1, 5, 62, 3]
After:  [1, 3, 3, 5, 62]

Test2)
5 1 1 1 1 6 5 4 7
Before:  [5, 1, 1, 1, 1, 6, 5, 4, 7]
After:  [1, 1, 1, 1, 4, 5, 5, 6, 7]

Test3)
3 5 2 0 1 2 2 3 0
Before:  [3, 5, 2, 0, 1, 2, 2, 3, 0]
After:  [0, 0, 1, 2, 2, 2, 3, 3, 5]

'''