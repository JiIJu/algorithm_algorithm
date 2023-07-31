# swea 1486 장훈이의 높은 선반
def dfs(idx,visit,check):
    global minv
    if (check)-B>=minv:
        return
    if idx==N:
        if 0<=(check)-B<minv:
            minv = abs(check-B)
        return


    if not visit[idx]:
        visit[idx] = 1
        dfs(idx+1,visit,check+data[idx])
        visit[idx] = 0
        dfs(idx+1,visit,check)

            # print(minv, visit,idx,check)
T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    data = list(map(int,input().split()))
    minv = 9999999
    dfs(0,[0]*N,0)
    print(f'#{tc} {minv}')