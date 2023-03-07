# 롤케이크자르기 프로그래머스
from collections import deque
def solution(topping):
    answer = 0
    stack = []
    chul,bro = {},{}
    for i in topping:
        if i in chul:
            chul[i]+=1
        else:
            chul[i] = 1
    # topping = deque(topping)
    for i in topping:
        if i in bro:
            bro[i]+=1
        else:
            bro[i]=1
        if i in chul and chul[i]>0:
            chul[i]-=1
            if chul[i]==0:
                del chul[i]
        if len(bro) == len(chul):
            answer+=1
            
    return answer
