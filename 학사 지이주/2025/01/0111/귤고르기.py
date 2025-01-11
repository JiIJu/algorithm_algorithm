def solution(k, tangerine):
    answer = 0
    temp = dict([])
    for i in tangerine:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] +=1
    a = sorted(list(temp.values()),reverse=True)
    b = 0
    for i in a:
        b+=1
        answer +=i
        if answer >=k:
            break
            
        
    return b