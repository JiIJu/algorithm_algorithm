# 7576 토마토

def bfs(i,j):
    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<M and data[nx][ny]==0:
                data[nx][ny]=data[x][y]+1
                q.append((nx,ny))

M , N = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = []
for i in range(N):
    for j in range(M):
        if data[i][j]==1:
            q.append((i,j))
maxv = 0
temp = 0


for i,j in q:
    bfs(i,j)

for i in data:
    if 0 in i:
        temp=1
        break
if temp:
    print(-1)
else:
    for i in data:
        maxv = max(maxv,max(i))
    print(maxv-1)
