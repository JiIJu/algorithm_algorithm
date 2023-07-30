# swea 4112 이상한 피라미드 탐험
data = [[0]*i for i in range(1,151)]
temp = 1
for i in range(150):
    for j in range(len(data[i])):
        data[i][j] =temp
        temp+=1
from collections import deque
def bfs(x,y):
    q = deque([[x,y,0]])
    visit = [[0]*i for i in range(1,151)]
    visit[x][y]=1
    while q:
        i,j,cnt = q.popleft()
        if data[i][j]==b:
            return cnt
        for d in range(6):
            ni = i + di[d]
            nj = j + dj[d]

            if 0<=ni<150 and 0<=nj<len(data[ni]) and not visit[ni][nj]:
                visit[ni][nj] = 1
                q.append((ni,nj,cnt+1))

T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input().split())

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]==a:
                start = [i,j]
            if data[i][j] ==b:
                finish = [i,j]
    di = [-1,-1,0,0,1,1]
    dj = [-1,0,-1,1,0,1]
    print(f'#{tc} {bfs(start[0],start[1])}')