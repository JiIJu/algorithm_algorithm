# 1931 회의실 배정
import sys
n = int(input())
data = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    data.append((a,b))
ans = 1
data.sort(key = lambda x:(x[1],x[0]))
# print(data)
a,b = data[0]
for i in range(1,n):
    c,d = data[i]
    if c>=b:
        ans+=1
        a,b= c,d

print(ans)