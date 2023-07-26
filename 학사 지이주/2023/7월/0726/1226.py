# swea 1226 미로1
from collections import deque
def bfs(a):
    q = deque([[a[0],a[1]]])
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<16 and 0<=nj<16 and data[ni][nj] != '1' and not visit[ni][nj]:
                visit[ni][nj]=1
                q.append((ni,nj))
                if [ni,nj] == finish:
                    return 1
    return 0

for tc in range(1,11):
    N = int(input())
    data = [list(input()) for _ in range(16)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    visit = [[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if data[i][j] == '2':
                start = [i,j]
            if data[i][j] == '3':
                finish = [i,j]
    visit[start[0]][start[1]] = 1
    print(f'#{tc} {bfs((start[0],start[1]))}')