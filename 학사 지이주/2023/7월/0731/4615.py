# swea 4615 재미있는 오셀로 게임

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [[0]*N for _ in range(N)]
    for i in range(N):
        a,b,c = map(int,input().split())
        data[a][b] = c
    print(data)