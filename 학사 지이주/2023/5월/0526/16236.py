# 11279 최대힙
import heapq
import sys
N = int(input())
data = []
for i in range(N):
    temp = int(sys.stdin.readline())
    if not temp:
        if not len(data):
            print(0)
        else:
            print(heapq.heappop(data)[1])
    else:
        heapq.heappush(data,(-temp,temp))