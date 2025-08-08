from collections import Counter

def solution(weights):
    answer = 0
    cnt = Counter(weights)

    for i , j in cnt.items():
        if j >= 2:
            answer += j*(j-1)//2
            
    for i in cnt:
        if i*2/3 in cnt:
            answer += cnt[i] * cnt[i*2/3]
        if i/2 in cnt:
            answer += cnt[i] * cnt[i/2]
        if i*3/4 in cnt:
            answer += cnt[i] * cnt[i*3/4]
        
    
    return answer