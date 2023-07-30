# swea 3234 준환이의 양팔저울
def dfs(left,right,index):
    global ans
    if left<right:
        return
    if index == N:
        ans+=1
        return
    if left>=critical:
        ans += fact[N-index]
        return
    for i in range(N):
        if not visit[i]:
            visit[i]=1
            dfs(left + data[i], right, index + 1)
            dfs(left,right+data[i],index+1)
            visit[i]=0
import math
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    # data.sort()
    visit = [0]*(N+1)
    fact = [math.factorial(i) * 2**i for i in range(11)]
    ans = 0
    critical = int(sum(data)/2+1)
    dfs(0,0,0)
    print(f'#{tc} {ans}')