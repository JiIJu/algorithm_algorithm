# swea 1868 파핑파핑 지뢰찾기
from collections import deque
def bfs(x,y):
    q = deque([[x,y]])
    visit[x][y] =1
    while q:
        i,j = q.popleft()
        if data[i][j] != '.':
            continue
        cnt = 0
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N and data[ni][nj] == '*':
                cnt+=1
        data[i][j] = cnt
        if not cnt:
            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == '.':
                    q.append((ni,nj))
                    visit[ni][nj]=1
        # print(q)
def check(i,j):
    cnt = 0
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == '*':
            cnt += 1
    if not cnt:
        return True
    else:
        return False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    di = [-1,-1,0,1,1,1,0,-1]
    dj = [0,1,1,1,0,-1,-1,-1]
    visit = [[0]*N for _ in range(N)]
    ans = 0
    a = []
    for i in range(N):
        for j in range(N):
            if check(i,j):
                a.append((i,j))
    for i,j in a:
        if data[i][j]=='.':
            bfs(i,j)
            ans+=1
    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                # print(i,j)
                bfs(i,j)
                ans+=1
    print(f'#{tc} {ans}')

