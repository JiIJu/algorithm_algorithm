# swea 1211 Ladder2
from collections import deque
def bfs(x,y):
    global minv , ans
    q = deque([[x,y,0]])
    visit = [[0]*100 for _ in range(100)]
    visit[x][y]=1
    while q:
        i,j,cnt= q.popleft()
        # print(i,j,cnt)
        if i==0:
            if minv>cnt:
                minv = cnt
                ans = j
                # print(f'{ans},{minv} @@@@@@@@@@@@@!#!@#!@#!@#!@#@#!@#!@#!@#!@#!@#!@#')
                return
        for d in range(3):
            ni = i + di[d]
            nj = j + dj[d]
            # print(ni,nj)
            if 0<=ni<100 and 0<=nj<100 and not visit[ni][nj] and data[ni][nj]==1:
                visit[ni][nj] = 1
                q.append((ni,nj,cnt+1))
                if d == 1 or d ==0:
                    break


for tc in range(1,11):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if data[-1][i] == 1:
            start.append(i)
    di = [0,0,-1]
    dj = [-1,1,0]
    minv , ans = 999999 , -1
    # print(data)
    for i in start:
        bfs(99,i)
    print(f'#{tc} {ans}')