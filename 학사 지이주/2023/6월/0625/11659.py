# 11659 구간 합 구하기 4
import sys
N , M = map(int,input().split())
data = list(map(int,input().split()))
ans = [0]*(N+1)

for i in range(1,N+1):
    ans[i] = ans[i-1]+data[i-1]
# print(ans)
for tc in range(M):
    a,b = map(int,sys.stdin.readline().split())
    print(ans[b]-ans[a-1])
