from collections import deque
def solution(numbers, target):
    answer = 0
    temp = deque([[0,0]])
    while temp:
        a,b = temp.popleft()
        if b == len(numbers):
            if a == target:
                answer+=1
        else:
            temp.append((a+numbers[b],b+1))
            temp.append((a-numbers[b],b+1))
    return answer