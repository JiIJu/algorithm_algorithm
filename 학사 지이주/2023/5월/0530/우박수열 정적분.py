def solution(k, ranges):
    answer = []
    data = []
    while k>1:
        data.append(k)
        if not k%2:
            k = k//2
        else:
            k = k*3+1
    data.append(1)
    n = len(data)
    area = []
    for i in range(n-1):
        area.append((data[i]+data[i+1])/2)
    for start,b in ranges:
        finish = n+b-1
        ans = 0
        if start == finish:
            answer.append(0)
        elif start > finish:
            answer.append(-1)
        else:
            for i in range(start,finish):
                ans+=area[i]
            answer.append(ans)
        
    return answer
