# swea 5607 조합
def power(a,b):
    if b==0:
        return 1
    if b%2:
        return (power(a,b//2)**2 * a) % 1234567891
    else:
        return (power(a,b//2)**2) % 1234567891

T = int(input())
for tc in range(1,T+1):
    N,R = map(int,input().split())
    fact = [0]*1000001
    fact[1] = 1
    fact[2] = 2
    for i in range(3,1000001):
        fact[i] = (i*fact[i-1])%1234567891



    ans = ((fact[N]%1234567891) * (power((fact[N-R]*fact[R])%1234567891,1234567891-2))%1234567891)%1234567891
    print(f'#{tc} {ans}')

