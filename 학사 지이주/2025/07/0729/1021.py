import sys
from collections import deque

n,m = map(int,sys.stdin.readline().strip().split())
target = list(map(int,input().split()))
data = deque([i for i in range(1,n+1)])
cnt = 0
for i in target:
    while data[0] != i:
        idx = data.index(i)
        if idx <= len(data)//2:
            data.rotate(-1)
        else:
            data.rotate(1)
        cnt +=1
    data.popleft()
print(cnt)  