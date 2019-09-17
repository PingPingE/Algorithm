from collections import Counter
s = input()
s = s.upper()
c = Counter(s)
vv = -1
for k,v in c.most_common(2):
    if vv==-1:
        vv = v
        ans = k
        continue
    if v== vv:
        print('?')
        break
    else:
        print(ans)
        break

