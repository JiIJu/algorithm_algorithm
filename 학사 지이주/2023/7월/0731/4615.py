# swea 4615 재미있는 오셀로 게임
from collections import deque
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [[0]*N for _ in range(N)]
    data[N//2-1][N//2-1] = 'W'
    data[N // 2-1][N // 2] = 'B'
    data[N // 2][N // 2-1] = 'B'
    data[N // 2][N // 2] = 'W'
    di = [-1,-1,0,1,1,1,0,-1]
    dj = [0,1,1,1,0,-1,-1,-1]

    for i in range(M):
        a,b,c = map(int,input().split())
        if c == 1:
            data[a-1][b-1] = 'B'
        else:
            data[a-1][b-1] = 'W'
        for d in range(8):
            ni = a-1+di[d]
            nj = b-1+dj[d]
            temp = [[ni,nj]]
            while 0<=ni<N and 0<=nj<N and data[ni][nj]!=0 and data[ni][nj] != data[a-1][b-1]:
                ni += di[d]
                nj += dj[d]
                temp.append([ni,nj])

            if len(temp)>1 and 0<=ni<N and 0<=nj<N and data[ni][nj] != 0:
                # print(temp)
                for x,y in temp:
                    data[x][y] = data[a-1][b-1]
    ansW,ansB = 0,0

    for i in data:
        for j in i:
            if j == 'W':
                ansW+=1
            elif j == 'B':
                ansB+=1
    # print(data)
    print(f'#{tc} {ansB} {ansW}')
