def solution(scores):
    answer = 1
    before = 0
    check = sum(scores[0])
    temp = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    for i in scores:
        if i[0]>temp[0] and i[1]>temp[1]:
            return -1
        if i[1]>=before:
            if i[0]+i[1]>check:
                answer+=1
            before = i[1]
    return answer
