from collections import deque
def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    dp = [[0]*(m) for _ in range(n)]
    
    for i,j in puddles:
        dp[j-1][i-1] = -1
    dp[0][0]=1
    
    for i in range(n):
        for j in range(m):
            if dp[i][j]==-1:
                dp[i][j]=0
                continue
            if i>0:
                dp[i][j] += dp[i-1][j]
            if j>0:
                dp[i][j] += dp[i][j-1]
            dp[i][j]= dp[i][j]%MOD 
    # print(dp)
    return dp[-1][-1]