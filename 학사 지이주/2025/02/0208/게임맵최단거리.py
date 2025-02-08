from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps) , len(maps[0])
    check = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        check.append(temp)
    di , dj = [-1,1,0,0] , [0,0,-1,1]
    queue = deque([[0,0,1]])
    while queue:
        i,j,cnt = queue.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and check[ni][nj]==0:
                queue.append([ni,nj,cnt+1])
                check[ni][nj]=1
                if ni==n-1 and nj==m-1:
                    return cnt+1
    
    return -1
