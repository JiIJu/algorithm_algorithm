# 2470 두용액
import sys
N = int(input())
data = list(map(int,input().split()))
data.sort()
left,right = 0,N-1
maxv = abs(data[0]+data[right])
small,large = 0,right
while left<right:
    mid = data[left]+data[right]
    if abs(mid)<=abs(maxv):
        small = left
        large = right
        maxv = abs(mid)
        if maxv ==0:
            break
    if mid<0:
        left +=1
    else:
        right-=1
print(data[small],data[large])
