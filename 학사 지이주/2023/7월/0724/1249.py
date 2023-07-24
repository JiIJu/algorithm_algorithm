# swea 1249 보급로
import sys
from collections import deque
def bfs():
    q = deque([[0,0]])
    visit[0][0] = 0
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N and int(data[ni][nj]) + int(visit[i][j]) < visit[ni][nj]:
                visit[ni][nj] = int(data[ni][nj]) + visit[i][j]
                q.append((ni,nj))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    visit = [[99999]*N for _ in range(N)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    bfs()

    print(f'#{tc} {visit[-1][-1]}')