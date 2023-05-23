# 1764 듣보잠
import sys
N , M = map(int,input().split())
hear = {}
see = {}
data = []
for i in range(N):
    a = sys.stdin.readline().rstrip()
    hear[a]=1

for i in range(M):
    a = sys.stdin.readline().rstrip()
    see[a]=1
if N>=M:
    for i in hear:
        if i in see:
            data.append(i)
else:
    for i in see:
        if i in hear:
            data.append(i)
# data = list(data)
data.sort()
print(len(data))
for i in data:
    if i:
        print(i)