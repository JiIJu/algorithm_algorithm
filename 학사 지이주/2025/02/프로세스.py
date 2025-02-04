# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
from collections import deque
def solution(priorities, location):
    answer = 0
    n = len(priorities)
    temp = deque([])
    for i in range(n):
        temp.append((priorities[i],i))
    ans = []
    cnt = 0
    while temp:
        a,b = temp.popleft()
        if temp:
            if a >= max(temp,key=lambda x:x[0])[0]:
                cnt+=1
                if b == location:
                    return cnt
            else:
                temp.append((a,b))
    
    return cnt+1