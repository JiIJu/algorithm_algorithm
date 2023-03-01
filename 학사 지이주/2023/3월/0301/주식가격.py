# 프로그래머스 주식가격
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    stack = deque()
    while prices:
        a = prices.popleft()
        temp = 0
        for i in prices:
            temp +=1
            if a >i:
                break
        answer.append(temp)
    
    return answer
