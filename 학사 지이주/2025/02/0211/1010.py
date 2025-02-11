
def fact(n):
    if n>1:
        return fact(n-1)*n
    else:
        return 1
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    
    a ,b= max(a,b),min(a,b)
    print(fact(a)//(fact(b)*fact(a-b)))