# 2110 공유기설치
import sys
N,C = map(int,input().split())
data = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
data.sort()
ans = 0
start,end = 1,data[-1]-data[0]
while start<=end:
    mid = (start+end)//2
    cnt = 1
    current = data[0]
    for i in range(1,N):
        if current+mid < data[i]:
            cnt+=1
            current=data[i]
    if cnt>=C:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)