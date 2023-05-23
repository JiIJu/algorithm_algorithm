# 1260 DFS와 BFS

N,M,V = map(int,input().split())
data = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
for i in range(1,N+1):
    data[i] = sorted(data[i])
visit1,visit2 = [0]*(N+1),[0]*(1+N)
def dfs(n):
    visit1[n] = 1
    print(n, end=' ')
    for i in data[n]:
        if not visit1[i]:
            dfs(i)
dfs(V)
from collections import deque
def bfs(V):
    q = deque([V])
    visit2[V]=1
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in data[a]:
            if not visit2[i]:
                visit2[i]=1
                q.append(i)
print()
bfs(V)
