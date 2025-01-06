def solution(n):
    answer = 0
    temp = [0] * (n+1)
    temp[1] = 1
    temp[2] = 1
    for i in range(2,n+1):
        temp[i] = (temp[i-1]+temp[i-2])
    
    return temp[n]%1234567
