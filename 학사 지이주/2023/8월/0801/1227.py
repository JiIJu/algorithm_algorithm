# swea 1227 미로2
from collections import deque
def bfs(x,y):
    q = deque([[x,y]])
    visit[x][y]=1
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<100 and 0<=nj<100 and not visit[ni][nj] and data[ni][nj] != '1':
                visit[ni][nj] = 1
                q.append((ni,nj))
                if data[ni][nj] == '3':
                    return 1
    return 0
for tc in range(1,11):
    T = int(input())
    data = [list(input()) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if data[i][j] == '2':
                start = [i,j]
            elif data[i][j] == '3':
                finish = [i,j]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    visit = [[0]*100 for _ in range(100)]
    print(f'#{tc} {bfs(start[0],start[1])}')