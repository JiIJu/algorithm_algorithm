# https://school.programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    data = deque([])
    for i in range(n):
        a = progresses[i]
        b = speeds[i]
        
        data.append(math.ceil((100-a)/b))
    temp = 0
    ans = 0
    a = data[0]
    if len(data)==1:
        return [1]
    while temp<len(data):
        b = data.popleft()
        if a>=b:
            ans+=1
        else:

            answer.append(ans)
            ans = 1
            a = b
    answer.append(ans)
    return answer