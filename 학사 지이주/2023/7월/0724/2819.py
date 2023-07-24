# swea 2819 격자판의 숫자 이어 붙이기
from collections import deque
def bfs(x,y,a):
    q = deque([[x,y,a]])
    while q:
        i,j,n = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if len(n)==7:
                ans.append(n)
            elif 0<=ni<4 and 0<=nj<4:
                q.append((ni,nj,n+str(data[ni][nj])))

T = int(input())
for tc in range(1,T+1):
    data = [list(map(int,input().split())) for _ in range(4)]
    ans = []
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    for i in range(4):
        for j in range(4):
            bfs(i,j,str(data[i][j]))
    print(f'#{tc} {len(set(ans))}')