# 1012 유기농배추
import sys
from collections import deque
def bfs(x,y):
    global visit
    q = deque([[x,y]])
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<M and 0<=nj<N and not visit[ni][nj] and data[ni][nj]:
                visit[ni][nj] = 1
                q.append([ni,nj])
T = int(input())

for tc in range(T):
    M,N,K = map(int,input().split())
    data = [[0]*N for _ in range(M)]
    for i in range(K):
        a,b = map(int,sys.stdin.readline().split())
        data[a][b] = 1
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    cnt = 0
    visit = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if not visit[i][j] and data[i][j]:
                # print(i,j)
                visit[i][j]=1
                bfs(i,j)
                # print(visit)
                cnt+=1
    print(cnt)
