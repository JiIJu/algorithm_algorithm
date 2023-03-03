# 게임맵 최단거리
from collections import deque
def solution(maps):
    global data
    data = maps
    answer = 0
    print(maps)
    def bfs(x,y):
        global answer,data
        n,m = len(data),len(data[0])
        q = [(x,y)]
        di = [-1,1,0,0]
        dj = [0,0,-1,1]
        visit = [[0]*m for _ in range(n)]
        print(n,m)
        while q:
            i,j = q.pop(0)
            for d in range(4):
                ni = i+di[d]
                nj = j+dj[d]
                if 0<=ni<n and 0<=nj<m and data[ni][nj]==1 and visit[ni][nj]==0:
                    visit[ni][nj] = 1
                    data[ni][nj] = data[i][j]+1
                    q.append((ni,nj))
    bfs(0,0)
    print(data)
    maxv = 0
    for i in data:
        maxv = max(max(i),maxv)
    if (data[-1][-1]==1):
        data[-1][-1]=-1
    
    return data[-1][-1]
