# https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3
import heapq
def solution(operations):
    answer = []
    temp = []
    temp2= []
    for i in operations:
        a,b = i.split()
        b = int(b)
        if a == 'I':
            heapq.heappush(temp,b)
            heapq.heappush(temp2,-b)
        elif a == 'D':
            if b == 1 and temp:
                c = heapq.heappop(temp2)
                temp.remove(-c)
            elif b == -1 and temp:
                c = heapq.heappop(temp)
                temp2.remove(-c)
    if not temp:
        return [0,0]
    else:
        return [max(temp),min(temp)]
    