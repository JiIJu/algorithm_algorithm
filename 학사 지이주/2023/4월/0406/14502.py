# 연구소
import sys
from collections import deque
def bfs():
    global maxv
    # q = deque(virus)
    temp = [i[:] for i in data]
    q = deque()
    for i in virus:
        q.append(i)
    n=0
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<M and temp[ni][nj]==0:
                temp[ni][nj]=2
                q.append([ni,nj])
    for i in temp:
        n+=i.count(0)
    maxv = max(maxv,n)
def wall(n):
    if n==3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if data[i][j]==0:
                data[i][j]=1
                wall(n+1)
                data[i][j]=0

N , M = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
virus = []
for i in range(N):
    for j in range(M):
        if data[i][j]==2:
            virus.append([i,j])
maxv = 0
wall(0)
print(maxv)