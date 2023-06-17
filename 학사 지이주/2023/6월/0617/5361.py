# 5361 트리의 부모찾기
import sys
from collections import deque
def bfs(n):
    visit = [0] * (N + 1)
    q = deque([n])
    visit[n]=1
    while q:
        a = q.popleft()
        for i in data[a]:
            if not visit[i]:
                visit[i]=1
                q.append(i)
                ans[i]=a
N = int(input())
data = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)
ans = [0]*(N+1)
# for i in range(1,N+1):
bfs(1)
print(ans)
for i in range(2,N+1):
    print(ans[i])
