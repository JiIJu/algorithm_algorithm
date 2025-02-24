from collections import deque

def check_diff(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt +=1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    queue = deque([[begin,0]])
    check = set(begin)
    while queue:
        a,b = queue.popleft()
        for i in words:
            if i not in check and check_diff(a,i):
                queue.append([i,b+1])
                check.add(i)
                if i == target:
                    answer = b+1
    if target not in words:
        return 0
    return answer
