def solution(clothes):
    answer = 1
    temp_dict = {}
    for i,j in clothes:
        if j not in temp_dict:
            temp_dict[j] = [i]
        else:
            temp_dict[j].append(i)
    for i in temp_dict:
        
        answer *= (len(temp_dict[i])+1)
    return answer-1