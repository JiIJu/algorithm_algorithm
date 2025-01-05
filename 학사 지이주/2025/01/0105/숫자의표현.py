def solution(n):
    answer = 1
    if n==2:
        return 1
    temp = 1
    while temp<=n//2+1:
        temp2 = 0
        for i in range(temp,n):
            temp2+=i
            if temp2==n:
                print(temp)
                answer+=1
                break
            elif temp2>n:
                break
        temp+=1
    return answer