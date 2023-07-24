# swea 1210 ladder1
from collections import deque

def bfs(start):
    q = deque([start])
    visit[start[0]][start[1]]=1
    while q:
        i,j = q.popleft()
        if i == 0:
            return j
        for d in range(3):
            ni = i+di[d]
            nj = j+dj[d]
            if 0<=ni<100 and 0<=nj<100 and data[ni][nj]==1 and not visit[ni][nj]:
                visit[ni][nj] = 1
                q.append((ni,nj))
                break

for tc in range(1,11):
    t = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    visit = [[0]*100 for _ in range(100)]
    for i in range(100):
        if data[-1][i]==2:
            start = i
            break
    di = [0,0,-1]
    dj = [-1,1,0]
    ans = bfs([99,start])
    print(f'#{tc} {ans}')