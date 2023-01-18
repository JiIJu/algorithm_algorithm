# 3273 두수의합
from itertools import combinations
n = int(input())

data = list(map(int,input().split()))
check = int(input())
ans = 0
data.sort()
temp = 0
left ,right = 0,n-1

while left<right:
    temp = data[left]+data[right]
    if temp==check:
        ans+=1
    elif temp<check:
        left+=1
        continue
    right-=1
print(ans)
