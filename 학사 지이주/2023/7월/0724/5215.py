# swea 5215 햄버거다이어트
from collections import deque
def dfs(idx,taste,cal):
    global maxv
    if cal >L:
        return
    if idx == N:
        maxv = max(maxv,taste)
        return
    dfs(idx+1,taste+data[idx][0],cal+data[idx][1])
    dfs(idx + 1, taste, cal)
T = int(input())

for tc in range(1,T+1):
    N,L = map(int,input().split())
    data = []
    ans = [0]*(L+1)
    for i in range(N):
        a,b = map(int,input().split())
        data.append((a,b))
    maxv = 0
    dfs(0,0,0)
    print(f'#{tc} {maxv}')