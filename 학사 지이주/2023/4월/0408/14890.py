# 경사로
import sys
N , L = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 0
for i in range(N):
    before = data[i][0]
    check = 1
    temp = 1
    for j in range(1,N):
        if data[i][j]==before:
            check+=1
        # 왼쪽이 더 큼
        elif data[i][j]-before==1 and check>=0:
            if check>=L:
                check = 1
                before = data[i][j]
            else:
                temp = 0
                break
        # 왼쪽이 더 큼
        elif before - data[i][j]==1 and check>=0:
            check = 1-L
            before =  data[i][j]
        else:
            temp=0
            break
    if temp:
        if check>=0:
            ans+=1
for i in range(N):
    before = data[0][i]
    check = 1
    temp = 1
    for j in range(1,N):
        if data[j][i]==before:
            check+=1
        # 왼쪽이 더 큼
        elif data[j][i]-before==1 and check>=0:
            if check>=L:
                check = 1
                before = data[j][i]
            else:
                temp = 0
                break
        # 왼쪽이 더 큼
        elif before - data[j][i]==1 and check>=0:
            check = 1-L
            before =  data[j][i]
        else:
            temp=0
            break
    if temp:
        if check>=0:
            ans+=1
print(ans)
