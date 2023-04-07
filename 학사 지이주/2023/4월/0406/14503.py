# 로봇청소기
import sys
from collections import deque
def bfs(x,y,now):
    q = deque([(x,y)])
    cnt = 0
    while q:
        temp = 0
        i,j = q.popleft()
        if data[i][j] == 0:
            data[i][j]=2
            q.append((i,j))
            # temp=1
            continue
        else:
            for d in range(1,5):
                ni = i+di[(now+d)%4]
                nj = j+dj[(now+d)%4]
                if 0<=ni<N and 0<=nj<M and data[ni][nj]==0:
                    q.append((ni,nj))
                    temp = 1
                    now = (now+d)%4
                    break
        if not temp:
            ni = i-di[now]
            nj = j-dj[now]
            if 0<=ni<N and 0<=nj<M and data[ni][nj]!=1:
                q.append((ni,nj))
            else:
                return
        # print(i,j,now)

N,M = map(int,input().split())
r,c,now = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# di = [-1,0,1,0]
# dj = [0,1,0,-1]
# 0 : 북 , 1 : 동 2 : 남 3:
di = [-1,0,1,0]
dj = [0,-1,0,1]
if now == 1:
    now = 3
elif now ==3:
    now = 1
bfs(r,c,now)
a = 0
# print(bfs(r,c,now))
for i in data:
    a+=i.count(2)
print(a)

