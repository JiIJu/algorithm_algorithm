from itertools import permutations
def solution(k, dungeons):
    answer = 0
    a = (list(permutations(dungeons)))
    for i in a:
        ans = 0
        temp = k
        for j in i:
            if temp-j[0]>=0 and temp-j[1]>=0:
                temp-=j[1]
                ans+=1
        answer = max(answer,ans)
    return answer

