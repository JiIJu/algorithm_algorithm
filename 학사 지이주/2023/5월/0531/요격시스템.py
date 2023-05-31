def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[1],x[0]))
    temp = 0
    n = len(targets)
    for i in range(n):
        if targets[i][0]>=temp:
            # print(targets[i])
            answer+=1
            temp = targets[i][1]
    return answer
