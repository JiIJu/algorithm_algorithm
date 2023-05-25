# 11047 동전0
import sys
N,K = map(int,input().split())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().rstrip()))
data.sort(reverse=True)
i=0
ans = 0
cnt = 0
while ans != K:
    if ans+data[i] <=K:
        ans += data[i]
        cnt +=1
    else:
        i+=1
print(cnt)