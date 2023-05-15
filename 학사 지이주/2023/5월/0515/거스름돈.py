def solution(n, money):
    answer = 0
    money.sort()
    data = [0]*(n+1)
    data[0]=1
    for i in money:
        for j in range(i,n+1):
            data[j] = (data[j-i]+data[j])%1000000007
    print(data)
    return data[n]
