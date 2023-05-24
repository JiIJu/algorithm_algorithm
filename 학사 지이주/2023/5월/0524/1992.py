# 1992 쿼드트리

N = int(input())
data = [list(input()) for _ in range(N)]

def comb(x,y,n):
    temp = data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if temp != data[i][j]:
                print('(',end='')
                comb(x,y,n//2)
                comb(x, y+n//2, n // 2)
                comb(x+n//2, y, n // 2)
                comb(x+n//2, y+n//2, n // 2)
                print(')',end='')
                return
    if temp=='0':
        print('0',end='')
    else:
        print('1',end='')
comb(0,0,N)