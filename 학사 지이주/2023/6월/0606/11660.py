# 11660 구간합 구하기5
import sys
N,M = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    ans[i][1]= data[i-1][0]
    for j in range(2,N+1):
        ans[i][j] = ans[i][j-1]+data[i-1][j-1]

for i in range(1,N+1):
    for j in range(1,N+1):
        ans[i][j] = ans[i-1][j] + ans[i][j]
for tc in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    # print(ans[x2][y2]-ans[x1][y1]+data[x2-1][y2-1])
    print(ans[x2][y2] - ans[x1-1][y2] - ans[x2][y1-1] + ans[x1-1][y1-1])