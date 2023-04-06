# 퇴사
import sys
N = int(input())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
maxv = 0
temp = [0]*(N+1)

for i in range(N-1,-1,-1):
    a,b = data[i]
    if a+i<=N:
        temp[i] = max(temp[i+1],b+temp[i+data[i][0]])
    else:
        temp[i] = temp[i+1]
print(temp[0])