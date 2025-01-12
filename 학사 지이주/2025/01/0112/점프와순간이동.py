def solution(n):
    ans = 0
    while n:
        if n%2:
            n-=1
            ans+=1
        else:
            while n%2==0:
                n=n//2
    return ans