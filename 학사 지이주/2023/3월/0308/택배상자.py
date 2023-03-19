# 프로그래머스 택배상자
from collections import deque
def solution(order):
    answer = 0
    order = deque(order)
    data = deque([i for i in range(1,len(order)+1)])
    stack = []
    i = 0
    while order and data:
        if data[0] == order[0]:
            data.popleft()
            order.popleft()
            answer+=1
        elif stack and stack[-1] == order[0]:
            order.popleft()
            stack.pop()
            answer+=1
        else:
            stack.append(data.popleft())
    while stack:
        if stack[-1] == order[0]:
            order.popleft()
            stack.pop()
            answer+=1
        else:
            break
        
        
    return answer
