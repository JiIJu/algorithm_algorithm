# 1927 최소힙
import sys
import heapq
N = int(input())
q = []
for i in range(N):
    x = int(sys.stdin.readline())
    if not x:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,x)