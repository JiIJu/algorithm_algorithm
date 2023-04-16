def solution(sequence, k):
    start,end = 0,0
    temp = sequence[start]
    n = len(sequence)
    answer = []
    while end<n:
        if temp==k:
            answer.append([start,end])
            temp-=sequence[start]
            start+=1
        elif temp<k:
            end+=1
            if end<n:
                temp+=sequence[end]
            
        else:
            temp-=sequence[start]
            start+=1
    return min(answer,key=lambda x:x[1]-x[0])
            