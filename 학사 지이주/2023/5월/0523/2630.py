# 2630 색종이 만들기
import sys
N = int(input())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = [0]*2

def solve(x,y,n):
    a = data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data[i][j] != a:
                for k in range(2):
                    for l in range(2):
                        solve(x+k*n//2,y+l*n//2,n//2)
                return
    if a==0:
        ans[0]+=1
    else:
        ans[1]+=1
solve(0,0,N)
for i in ans:
    print(i)