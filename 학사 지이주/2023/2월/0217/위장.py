def solution(clothes):
    answer=1
    data = {}    
    for i,j in clothes:
        if j not in data:
            data[j] = []
    temp = 1
    for i,j in clothes:
        if i not in data[j]:
            data[j].append(i)
    
    for i in data.keys():
        answer *= len(data[i])+1
    return answer-1
