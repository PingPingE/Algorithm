N = int(input())
nums = list(map(int, input().split()))
s,e=0,0
maxx =0
while e+1<len(nums):
    if nums[e]<=nums[e+1]:
        e+=1
    else:
      maxx=max(maxx, e-s+1)
      s=e
      e+=1
maxx=max(maxx, e-s+1)
print(maxx)