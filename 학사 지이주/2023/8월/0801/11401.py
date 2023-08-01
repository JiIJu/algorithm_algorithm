# 백준 11401 이항계수 3
def power(a,b):
    if b==0:
        return 1
    if b%2:
        return (power(a,b//2)**2 * a) % temp
    else:
        return (power(a,b//2)**2) % temp
N,K = map(int,input().split())
fact = [0] * 4000001
fact[0]=1
fact[1]=1
fact[2]=2
temp = 1000000007
for i in range(3,N+1):
    fact[i] = (i*fact[i-1])%temp
ans = ((fact[N]%temp) * ((power((fact[N-K]*fact[K])%temp,temp-2))%temp))%temp
print(ans)