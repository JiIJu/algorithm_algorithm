import sys
import heapq
"""
파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공한다.

모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데, 내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태
"""
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int,input().split())
    heapq.heappush(arr,(b,a)) # heapq.heappush(heap, item) : item을 heap에 추가

ans = 0
now = 0

while arr:
    a,b = heapq.heappop(arr) # heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
    if b >= now: 
        now = a
        ans += 1

print(ans)
