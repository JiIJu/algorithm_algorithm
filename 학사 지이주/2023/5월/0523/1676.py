# 1676 팩토리얼 0의 개수

def fact(n):
    cnt = 0
    if n>=2:
        num[n] = num[n-1]*n
        while not num[n]%10:
            num[n] = num[n]//10
            cnt +=1
        ans[n] = ans[n-1]+cnt
    else:
        num[n] = 1
N = int(input())
num = [0] * (501)
num[1] = 1
ans = [0] * (501)

if N>2:
    for i in range(2,N+1):
        fact(i)
    print(ans[N])
else:
    print(0)

