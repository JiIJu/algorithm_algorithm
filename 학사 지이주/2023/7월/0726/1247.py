# swea 1247 최적경로
def dfs(now,check,visit):
    global minv
    if check>=minv:
        return
    if sum(visit)==N:
        minv = min(minv,check + abs(now[0]-home[0])+abs(now[1]-home[1]))
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs(data[i],check+abs(now[0]-data[i][0])+abs(now[1]-data[i][1]),visit)
            visit[i] = 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int,input().split()))
    company = [temp[0],temp[1]]
    home = [temp [2],temp[3]]
    data = []
    for i in range(4,N*2+4,2):
        data.append([temp[i],temp[i+1]])
    minv = 9999999
    dfs((company[0],company[1]),0,[0]*N)
    print(f'#{tc} {minv}')
