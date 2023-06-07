# 15650 N과M(2)
from itertools import combinations
N,M = map(int,input().split())
data = [i for i in range(1,N+1)]

ans = sorted(list(combinations(data,M)))
for i in ans:
    print(*i)