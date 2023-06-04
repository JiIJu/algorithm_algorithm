# 1629 곱셈
def solve(a,b,c):
    if b==1:
        return a%c
    elif b%2:
        return ((solve(a,b//2,c)**2)*a)%c
    elif b%2==0:
        return (solve(a, b // 2, c)**2) % c
A,B,C = map(int,input().split())


print(solve(A,B,C))