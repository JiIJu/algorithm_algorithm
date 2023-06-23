# 16928 뱀과 사다리 게임
import sys
from collections import deque
N,M = map(int,input().split())
data = [i for i in range(101)]
for i in range(N+M):
    a,b = map(int,sys.stdin.readline().split())
    data[a]=b
visit = [0]*101

def bfs(n):
    q = deque([n])
    visit[n]=0
    while q:
        i = q.popleft()
        for d in range(1,7):
            if i+d<=100:
                temp = data[i+d]
                if visit[temp]==0:
                    q.append(temp)
                    visit[temp] = visit[i]+1
bfs(1)

print(visit[-1])
