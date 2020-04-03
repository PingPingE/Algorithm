def sol():
    st = []
    for i in range(len(A)):
        if A[i] in['(', '[', '{']:
            st.append(i)
        else:
            if len(st) == 0:
                return 0
            else:
                st.pop()
    return 1 if len(st) ==0 else 0
A = list(input())
print(sol())