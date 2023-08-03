# swea 1494 사랑의 카운슬러
from itertools import combinations
def comb(visit,idx,num):
    if num == N//2:
        solve(visit)
        return
    for i in range(idx,N):
        visit[i]=1
        comb(visit,i+1,num+1)
        visit[i]=0
def solve(visit):
    global minv
    A = [0,0]
    B = [0,0]
    for i in range(N):
        if visit[i]:
            A[0] += data[i][0]
            A[1] += data[i][1]
        else:
            B[0] += data[i][0]
            B[1] += data[i][1]
    minv = min(minv,(A[0]-B[0])**2 + (A[1]-B[1])**2)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = []
    for i in range(N):
        a,b = map(int,input().split())
        data.append((a,b))
    minv = float('inf')
    comb([0]*N,0,0)
    print(f'#{tc} {minv}')