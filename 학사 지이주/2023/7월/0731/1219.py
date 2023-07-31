# swea 1219 길찾기
from collections import deque
def bfs():
    q = deque([0])
    visit = [0]*100
    visit[0]=1
    while q:
        i = q.popleft()
        if i == 99:
            return 1
        if data1[i] != -1 and not visit[data1[i]]:
            visit[data1[i]] = 1
            q.append(data1[i])
        if data2[i] != -1 and not visit[data2[i]]:
            visit[data2[i]] = 1
            q.append(data2[i])
    return 0


for tc in range(1,11):
    T , N = map(int,input().split())
    node = list(map(int,input().split()))
    data1,data2 = [-1]*100,[-1]*100
    for i in range(0,2*N,2):
        if data1[node[i]] == -1:
            data1[node[i]] = node[i+1]
        else:
            data2[node[i]] = node[i+1]
    print(f'#{tc} {bfs()}')