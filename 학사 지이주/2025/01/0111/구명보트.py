from collections import deque
def solution(people, limit):
    answer = 0
    people = sorted(people,reverse=True)
    i,j=0,len(people)-1

    while j>=i:
        # print(i,j)
        # print(people[i],people[j])
        if limit>=people[i]+people[j]:
            j-=1
        i+=1

        answer+=1
        
    
    return answer