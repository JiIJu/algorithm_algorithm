from collections import deque
def bfs(start,visit,n,computers):
    visit[start] = True
    queue = deque([start])
    while queue:
        a = queue.popleft()
        for i in range(n):
            if visit[i] == False and computers[a][i]:
                queue.append(i)
                visit[i]=True

def solution(n, computers):
    answer = 0
    queue = deque([])
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            bfs(i,visit,n,computers)
            answer+=1
    return answer