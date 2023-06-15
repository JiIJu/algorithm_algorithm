# 2178 미로탐색
import sys
N,M = map(int,input().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
visit = [[0]*M for _ in range(N)]
from collections import deque
def bfs(a,b):
    visit[a][b]=1
    q = deque([[a,b]])
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<M and data[ni][nj] == '1' and not visit[ni][nj]:
                visit[ni][nj] = visit[i][j]+1
                q.append((ni,nj))
bfs(0,0)
print(visit[-1][-1])
