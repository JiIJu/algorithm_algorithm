import sys

sys.setrecursionlimit(10 ** 8)


def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    print(N, M)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    minv = 9999999

    # visit = [[0]*M for _ in range(N)]
    def dfs(x, y, cnt, minv):
        if board[x][y] == 'G':
            minv = min(minv, cnt)
            return
        for d in range(4):
            i, j = x, y
            # while 0<=ni<N and 0<=nj<M and not visit[ni][nj] and board[ni][nj]!='D':
            while 0 <= i + di[d] < N and 0 <= j + dj[d] < M and board[i + di[d]][j + dj[d]] != 'D':
                i = i + di[d]
                j = j + dj[d]

            dfs(i, j, cnt + 1, minv)

    dfs(start[0], start[1], 0, minv)
    print(minv)
    return minv