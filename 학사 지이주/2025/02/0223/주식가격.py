from collections import deque
def solution(prices):
    answer = []
    temp = deque(prices)
    n = len(prices)
    while temp:
        a = temp.popleft()
        cnt = 0
        for i in temp:
            if i < a:
                cnt+=1
                break
            else:
                cnt+=1
        answer.append(cnt)
    return answer