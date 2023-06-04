# 1149 RGB거리
import sys
N = int(input())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = [[999999]*3 for _ in range(N)]
ans[0][0],ans[0][1],ans[0][2] = data[0][0],data[0][1],data[0][2]

for i in range(1,N):
    ans[i][0] = min(ans[i-1][1]+data[i][0],ans[i-1][2]+data[i][0])
    ans[i][1] = min(ans[i - 1][0] + data[i][1], ans[i - 1][2] + data[i][1])
    ans[i][2] = min(ans[i - 1][0] + data[i][2], ans[i - 1][1] + data[i][2])
print(min(ans[-1]))
