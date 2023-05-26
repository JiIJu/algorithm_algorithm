# 11286 절댓값 힙

import sys
import heapq

N = int(input())
data = []
for i in range(N):
    x = int(sys.stdin.readline())
    if not x:
        if not len(data):
            print(0)
        else:
            print(heapq.heappop(data)[1])
    else:
        heapq.heappush(data,(abs(x),x))