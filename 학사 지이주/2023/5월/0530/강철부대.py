from collections import deque
def bfs(a,b,goal,data,check):
    q = deque([[a,b]])
    while q:
        a,cnt = q.popleft()
        # print(a,cnt)
        if check[a] > cnt:
            check[a] = cnt
        for d in data[a]:
            if check[d]>cnt+1:
                check[d] = cnt+1
                q.append((d,cnt+1))
def solution(n, roads, sources, destination):
    answer = []
    data = [[] for _ in range(n+1)]
    for a,b in roads:
        data[a].append(b)
        data[b].append(a)
    check = [999999]*(n+1)
    for i in sources:
        bfs(destination,0,i,data,check)
    for i in sources:
        if check[i] < 999999:
            answer.append(check[i])
        else:
            answer.append(-1)
    return answer
