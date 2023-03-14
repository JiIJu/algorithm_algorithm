def solution(board):
    answer = 0
    n,m = len(board),len(board[0])
    data = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i-1][j-1]:
                data[i][j] = min(data[i-1][j],data[i][j-1],data[i-1][j-1])+1
            if data[i][j]>answer:
                answer = data[i][j]
    
    return (answer)**2
