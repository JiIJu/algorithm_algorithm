from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        i2 = deque(i)
        temp = deque(skill)
        now = []
        check = 1
        for j in i:
            if j not in temp:
                pass
            else:
                if j not in now and j==temp[0]:
                    now.append(temp.popleft()) 
                elif j in now and i2[0] == j:
                    i2.popleft()
                else:
                    check = 0
                    break
            # print(i ,j , i2 , now)

        if check:
            
            answer+=1
    return answer
