from collections import deque
def bfs(visit,start,data):
    q = deque([start])
    visit[start] = 1
    result = 1
    while q:
        now = q.popleft()
        for i in data[now]:
            if not visit[i]:
                result +=1
                visit[i] = 1
                q.append(i)
    return result
def solution(n, wires):
    global minv
    answer = 999999
    data = [[] for _ in range(n+1)]
    minv = 999999
    for a,b in wires:
        data[a].append(b)
        data[b].append(a)
    
    for a,b in wires:
        visit = [0] * (n+1)
        visit[b] = 1
        temp = bfs(visit,a,data)
        answer = min(abs(2*temp-n),answer)
        
        
    return answer
