import copy
def solution(want, number, discount):
    answer = 0
    sum_num = sum(number)
    n = len(discount)
    # if discount[1] in want:
    #     print(number[want.index(discount[3])])
    for i in range(n-9):
        temp = copy.deepcopy(number)
        for j in range(i,i+10):
            if discount[j] in want and temp[want.index(discount[j])]>=1:
                temp[want.index(discount[j])] -=1
        if sum(temp)==0:
            answer+=1
            # print(i)
    
    return answer