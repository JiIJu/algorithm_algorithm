# 7569 토마토
import sys
from collections import deque

def bfs():
    global maxv
    q = deque()
    for i in check:
        q.append((i[0],i[1],i[2],0))
    while q:
        i,j,k,cnt = q.popleft()
        maxv = max(maxv,cnt)
        for d in range(6):
            ni = i + di[d]
            nj = j + dj[d]
            nk = k + dk[d]
            if 0<=ni<N and 0<=nj<M and 0<=nk<H and not data[nk][ni][nj]:
                data[nk][ni][nj]=1
                q.append((ni,nj,nk,cnt+1))

M,N,H = map(int,input().split())
data = [[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        data[i].append(list(map(int,sys.stdin.readline().split())))

di = [-1,1,0,0,0,0]
dj = [0,0,-1,1,0,0]
dk = [0,0,0,0,-1,1]

visit = [[0]*M for _ in range(H)]
maxv = 0

check = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k]==1:
                check.append((j,k,i))
temp = 1
bfs()

for i in range(H):
    for j in range(N):
        if 0 in data[i][j]:
            temp = 0
            print(-1)
            break
    if not temp:
        break
if temp:
    print(maxv)