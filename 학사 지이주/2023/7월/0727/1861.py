# swea 1861 정사각형 방
from collections import deque
def bfs(x,y):
    global maxv , check
    q = deque([[x,y,1]])
    # visit = []
    # visit.append([x,y])
    while q:
        i,j,cnt = q.popleft()
        if cnt > maxv:
            maxv = cnt
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N  and (data[i][j]-data[ni][nj])==-1:
                q.append((ni,nj,cnt+1))
                # visit.append([ni,nj])
def bfs2(x,y):
    global maxv , check
    q = deque([[x,y,1]])
    while q:
        i,j,cnt = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N  and (data[i][j]-data[ni][nj])==-1:
                q.append((ni,nj,cnt+1))
                if cnt+1 == maxv:
                    # print(ni, nj)
                    check = min(check, data[x][y])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    maxv = 0
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    check = 999999999
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    for i in range(N):
        for j in range(N):
            bfs2(i,j)

    print(f'#{tc} {check} {maxv}')