from collections import deque
def solution(order):
    answer = 0
    data = []
    for i in range(1,len(order)+1):
        data.append(i)
        while data and data[-1] == order[answer]:
            data.pop()
            answer+=1
    
    
    return answer