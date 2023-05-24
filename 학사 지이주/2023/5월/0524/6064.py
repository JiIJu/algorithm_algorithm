# 6064 카잉달력
import sys
def gcd(a,b):
    if b>a:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a
T= int(input())
for tc in range(T):
    M,N,x,y = map(int,sys.stdin.readline().rstrip().split())
    i=1
    temp = 0
    num = N * M // gcd(N,M)
    while x<=N*M:
        if x%N == y%N:
            print(x)
            temp=1
            break
        x+=M

    if not temp:
        print(-1)

'''       
15
40000 39999 39999 39998
40000 39999 40000 39999
40000 40000 40000 39999
40000 39998 40000 39997
39999 2 39998 2
3 40000 3 39999
40000 3 40000 3
8 2 4 2
10 12 2 12
12 10 12 10
12 10 1 1
12 6 12 6
10 1 5 1
1 10 1 5
1 1 1 1'''