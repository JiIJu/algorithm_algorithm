#1188 음식평론가

N,M = map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

print(M-gcd(N,M))
