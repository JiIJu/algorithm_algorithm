# 1003 피보나치 함수
def fib(n):
    if n>2:
        num[n] = num[n-1] + num[n-2]
    else:
        num[n] = 1

T = int(input())
for tc in range(T):
    N = int(input())
    num = [0]*(N+1)
    for i in range(1,N+1):
        fib(i)
    if N>=1:
        print(f'{num[-2]} {num[-1]}')
    else:
        print(f'1 0')
