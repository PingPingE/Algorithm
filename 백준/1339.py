# import sys
# N = int(input())
# arr = []
# cnt = 9
# m = {}
# start = 10
# for _ in range(N):
#     li = sys.stdin.readline().rstrip()
#     arr.append(li)
#
# A = [[]*10 for _ in range(10)]
# for i in range(N):
#     k = 10 - len(arr[i])
#     if start > k:
#         start = k
#     for j in arr[i]:
#         A[k].append(j)
#         k+= 1
#
# for e in range(10):
#     if len(A[e]) < 1:
#         continue
#     for ee in A[e]:
#         if ee in m:
#             m[ee] += 1
#         else:
#             m[ee] = 1
#     for key in m:
#         m[key] *= 10
#
# result = []
# for k,v in m.items():
#     result.append([v,k])
# result.sort(reverse = True)
# for g in result:
#     m[g[1]] = cnt
#     cnt -= 1
#
#
# #적용
# res = 0
# for g in range(N):
#     n = len(arr[g])-1
#     for h in arr[g]:
#         res += m[h]*(10**n)
#         n -= 1
# print(res)

#숏코딩
n=int(input())
w,r,s=[0]*26,0,9
for i in range(n):
    li=input()
    for i in range(len(li)):
        w[ord(li[i])-ord('A')]+=10**(len(li)-i-1)
w.sort(reverse=True)
for i in w:
	r,s=r+i*s,s-1
print(r)


# #숏코딩2
# n = int(input())
# dic = {}
# for i in range(n):
# 	k = list(reversed(input()))
# 	t = 1
# 	for c in k:
# 		if c in dic:
# 			dic[c] += t
# 		else:
# 			dic[c] = t
# 		t *= 10
# li = list(dic.items())
# li.sort(key=lambda x:x[1], reverse=True)
# s = 0
# t = 9
# for i in li:
# 	s += t*i[1]
# 	t -= 1
# print(s)