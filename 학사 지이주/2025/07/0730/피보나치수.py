def solution(n):
    answer = 0
    data = [0]*100001
    data[1] = 1
    data[2] = 1
    
    for i in range(3,100001):
        data[i] = (data[i-2] + data[i-1])%1234567
    return data[n]