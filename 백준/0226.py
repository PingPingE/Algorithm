n = int(input())
start = 2
mult = 6
cnt = 1
if n == 1:
    print(cnt)
else:
    while 1:
        if n not in range(start,(start+mult)):
            start = start+mult
            mult = mult+6
            cnt = cnt+1
        else:
            print(cnt+1)
            break

    
