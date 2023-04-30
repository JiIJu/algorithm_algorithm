from collections import deque
def solution(maps):
    def bfs1(i,j):
        q = deque([[i,j]])
        visit = [[0]*m for _ in range(n)]
        a = 0
        while q:
            x,y = q.popleft()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 and new_maps[nx][ny]!='X':
                    visit[nx][ny] = visit[x][y]+1
                    q.append((nx,ny))
                if [nx,ny] == lever:
                    return visit[nx][ny]
    def bfs2(i,j):
        q = deque([[i,j]])
        visit = [[0]*m for _ in range(n)]
        a = 0
        while q:
            x,y = q.popleft()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 and new_maps[nx][ny]!='X':
                    visit[nx][ny] = visit[x][y]+1
                    q.append((nx,ny))
                if [nx,ny] == finish:
                    return visit[nx][ny]
                    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n ,m= len(maps),len(maps[0])
    new_maps = []
    for i in maps:
        new_maps.append(list(i))
    temp =0
    for i in range(n):
        for j in range(m):
            if new_maps[i][j]=='S':
                start = [i,j]
                temp+=1
            elif new_maps[i][j] == 'L':
                lever = [i,j]
                temp+=1
            elif new_maps[i][j] == 'E':
                finish = [i,j]
                temp+=1
        if temp==3:
            break
    a = bfs1(start[0],start[1])
    b = bfs2(lever[0],lever[1])
    if a and b:
        return a+b
    else:
        return -1
    
