# 1932 정수 삼각형
import sys
n = int(input())
tri = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
data = [[0]*i for i in range(1,n+1)]
data[0][0] = tri[0][0]
for i in range(1,n):
    data[i][0]= tri[i][0] + data[i-1][0]
    data[i][-1] = tri[i][-1] + data[i-1][-1]
for i in range(2,n):
    for j in range(1,i):
        data[i][j] = max(data[i-1][j],data[i-1][j-1])+tri[i][j]
print(max(data[-1]))