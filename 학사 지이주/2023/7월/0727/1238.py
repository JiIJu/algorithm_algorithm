# swea 1238 contact
from collections import deque
def bfs(s):
    global maxv
    q = deque([[s,0]])
    while q:
        i,cnt = q.popleft()
        if maxv<cnt:
            maxv = cnt
        # if data[i]:
        for d in data[i]:
            if not visit[d]:
                visit[d]=1
                q.append((d,cnt+1))
                ans[cnt+1].append(d)


for tc in range(1,11):
    n,s = map(int,input().split())
    temp = list(map(int,input().split()))
    data = [[] for _ in range(101)]
    for i in range(0,n,2):
        data[temp[i]].append(temp[i+1])
    # print(data)
    visit = [0] * 101
    ans = [[] for _ in range(101)]
    maxv = 0
    bfs(s)
    print(f'#{tc} {max(ans[maxv])}')