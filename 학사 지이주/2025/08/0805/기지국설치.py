import math
def solution(n, stations, w):
    answer = 0
    cover =  2 * w +1 
    position = 1
    
    for i in stations:
        left = i - w
        if position < left:
            gap = left - position
            answer += math.ceil(gap/cover)
        position = i + w + 1
    
    if position <= n:
        left = n - position + 1
        answer += math.ceil((left)/cover)
        

    return answer
