def solution(n):
    answer = 0
    temp = [0]*(n+1)
    temp[1]=1
    if n==1:
        return 1
    temp[2] = 2
    
    if n==2:
        return 2
    elif n==3:
        return 3
    for i in range(3,n+1):
        temp[i] = (temp[i-1]+temp[i-2])%1234567
    
    return temp[n]