from collections import deque
def solution(progresses, speeds):
    answer = []
    data = deque([])
    n = len(progresses)
    for i in range(n):
        a,b = progresses[i],speeds[i]
        if (100-a)%b:
            c = (100-a)//b+1
        else:
            c = (100-a)//b
        data.append(c)
    temp = data.popleft()
    cnt = 1
    # print(temp)
    while data:
        if temp>=data[0]:
            data.popleft()
            cnt+=1
        else:
            answer.append(cnt)
            temp = data.popleft()
            cnt = 1
    answer.append(cnt)
    return answer
