def dfs(numbers, start, path, answer):
    print(path)
    if len(path) == 2:
        answer.add(sum(path))
        return
    
    for i in range(start, len(numbers)):
        dfs(numbers, i, path + [numbers[i]], answer)
    
def solution(numbers):
    answer = set()
    dfs(numbers, 0, [], answer)
    
    return sorted(list(answer))

from collections import deque

def solution(numbers):
    answer = set()
    queue = deque()
    queue.append((0, []))  # (start_index, 현재 path)

    while queue:
        
        start, path = queue.popleft()
        print(path)
        if len(path) == 2:
            answer.add(sum(path))
            continue  # 더 이상 안 들어가도 됨

        for i in range(start, len(numbers)):
            queue.append((i + 1, path + [numbers[i]]))

    return sorted(list(answer))


## https://school.programmers.co.kr/learn/courses/30/lessons/68644
