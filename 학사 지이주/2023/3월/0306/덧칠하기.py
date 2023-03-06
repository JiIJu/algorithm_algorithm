def solution(n, m, section):
    answer = 0
    now ,finish = section[0]-1,section[-1]
    
    for i in range(len(section)):
        if now<section[i]:
            now = section[i]+m-1
            answer+=1
    return answer
