# 2667 단지번호붙이기

N = int(input())
visit = [[0]*N for _ in range(N)]
data = [list(input()) for _ in range(N)]
from collections import deque
def bfs(x,y,cnt):
    q = deque([[x,y]])
    visit[x][y] = cnt
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N and not visit[ni][nj] and data[ni][nj]=='1':
                visit[ni][nj] = cnt
                q.append((ni,nj))

di = [-1,1,0,0]
dj = [0,0,-1,1]
cnt=0
for i in range(N):
    for j in range(N):
        if data[i][j]=='1' and not visit[i][j]:
            cnt += 1
            bfs(i,j,cnt)
num = [0]*(cnt+1)
print(cnt)
for i in range(1,cnt+1):
    for j in range(N):
        for k in range(N):
            if visit[j][k]==i:
                num[i]+=1
num.sort()
for i in range(1,cnt+1):
    print(num[i])