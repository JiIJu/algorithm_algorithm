# 프로그래머스 기능개발
def solution(progresses, speeds):
    from collections import deque
    answer = []
    data = [0]*len(progresses)
    for i in range(len(progresses)):
        data[i] = 100 - progresses[i]
    date = [0]*len(progresses)
    for i in range(len(progresses)):
        if data[i]%speeds[i]:
            temp = data[i]//speeds[i]+1
        else:
            temp = data[i]//speeds[i]
        date[i] = temp
    date = deque(date)
    print(date)
    a = deque()
    res = 1
    q = 0
    while date:
        if q<date[0]:
            q = date.popleft()
        else:
            date.popleft()
        if date and date[0]>q:
            answer.append(res)
            res = 1
        elif not date:
            break
        else:
            res+=1
    answer.append(res)
    return answer
