# 14500 테트로미노
import sys

def dfs(x,y,num,cnt):
    global maxv
    if cnt==4:
        maxv = max(maxv,num)
        return
    for d in range(4):
        ni = x + di[d]
        nj = y + dj[d]
        if 0<=ni<N and 0<=nj<M and not visit[ni][nj]:
            if cnt==2:
                visit[ni][nj] = 1
                dfs(x,y,num+data[ni][nj],cnt+1)
                visit[ni][nj] = 0

            visit[ni][nj]=1
            dfs(ni,nj,num+data[ni][nj],cnt+1)
            visit[ni][nj]=0
N,M = map(int,input().split())

data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
maxv = 0
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visit[i][j]=1
        dfs(i,j,data[i][j],1)
        visit[i][j] = 0
print(maxv)