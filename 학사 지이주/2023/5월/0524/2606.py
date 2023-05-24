# 2606 바이러스
import sys
N = int(input())
M = int(input())
data = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)
visit = [0]*(N+1)
from collections import deque

def bfs(n):
    q = deque([n])
    while q:
        a = q.popleft()
        for i in data[a]:
            if not visit[i]:
                visit[i]=1
                q.append(i)
bfs(1)
print(sum(visit)-1)