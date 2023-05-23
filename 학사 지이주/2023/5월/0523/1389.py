# 1389 케빈베이컨의 6단계 법칙
import sys
N , M = map(int,input().split())
data = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    if b not in data[a]:
        data[a].append(b)
    if a not in data[b]:
        data[b].append(a)
minv = 9999999
ans = [0]*(N+1)
from collections import deque
def bfs(n,visit,m):
    global minv
    q = deque([[n,m]])
    while q:
        a,b = q.popleft()
        for i in data[a]:
            if not visit[i] and i !=n:
                visit[i]=b+1
                q.append((i,b+1))

    ans[n] = sum(visit)
ans[0] = 999999
for i in range(1,N+1):
    bfs(i,[0]*(N+1),0)
z = min(ans)
for i in range(1,N+1):
    if i == ans.index(z):
        print(i)
        break
