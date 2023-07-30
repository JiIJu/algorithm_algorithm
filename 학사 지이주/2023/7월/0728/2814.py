# swea 2814 최장경로
from collections import deque
def dfs(a,cnt):
    global maxv

    if cnt > maxv:
        maxv = cnt
    for d in data[a]:
        if not visit[d]:
            visit[d]=1
            dfs(d,cnt+1)
            visit[d]=0


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [[] for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        data[a].append(b)
        data[b].append(a)
    for i in range(N):
        data[i].sort()
    visit = [0]*(N+1)
    maxv = 0
    for i in range(1,N+1):
        dfs(i,1)
    print(f'#{tc} {maxv}')

