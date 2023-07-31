# swea 11315 오목판정
from collections import deque
def bfs(x,y):
    direction = []
    for i in range(8):
        if 0<=x+di[i]<N and 0<=y+dj[i]<N and data[x+di[i]][y+dj[i]] == 'o':
            direction.append(i)
    q = deque([])
    for d in direction:
        q.append((x,y,1,d))
    while q:
        i,j,cnt ,d = q.popleft()
        # print(i,j,cnt,d)
        if cnt>=5:
            return 1
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<N and  data[ni][nj]=='o':
            q.append((ni,nj,cnt+1,d))
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    di = [-1,-1,0,1,1,1,0,-1]
    dj = [0,1,1,1,0,-1,-1,-1]
    temp = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]=='o':
                temp = bfs(i,j)
                if temp:
                    break
        if temp:
            break
    if temp:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
