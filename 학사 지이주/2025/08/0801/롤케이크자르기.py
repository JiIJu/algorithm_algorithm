def solution(topping):
    answer = 0
    n = len(topping)
    temp1 = dict([])
    temp2 = dict([])
    
    for i in range(n):
        if topping[i] not in temp1:
            temp1[topping[i]] = 1
        else:
            temp1[topping[i]] +=1
    
    for i in range(n-1,0,-1):
        if topping[i] not in temp2:
            temp2[topping[i]] = 1
        else:
            temp2[topping[i]] +=1
        if temp1[topping[i]] == 1:
            del temp1[topping[i]]
        else:
            temp1[topping[i]] -=1
        if len(temp1) == len(temp2):
            answer+=1
    return answer