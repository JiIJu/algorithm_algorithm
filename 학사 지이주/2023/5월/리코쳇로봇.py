from collections import deque
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    visit = [[999999]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                start = (i,j)
                visit[i][j] = 0

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    minv = 9999999

    # def bfs(x,y,cnt,minv):
    q = deque([[start[0],start[1],0]])
    while q:
        a,b,c = q.popleft()
        if board[a][b]=='G':
            minv = min(minv,c)
            return minv
        for d in range(4):
            i,j = a,b
            # while 0<=ni<N and 0<=nj<M and not visit[ni][nj] and board[ni][nj]!='D':
            while 0<=i+di[d]<N and 0<=j+dj[d]<M and board[i+di[d]][j+dj[d]] != 'D':
                i = i + di[d]
                j = j + dj[d]
            if visit[i][j]>c+1:
                visit[i][j] = c+1
                q.append((i,j,c+1))
        
    # bfs(start[0],start[1],0,minv)
    return -1
