# 11004 K번째수
import heapq

n,k = map(int,input().split())
data = list(map(int,input().split()))
data = heapq.heapify(data)
for i in range(k-1):
    heapq.heappop(data)
print(data[0])
