from collections import deque
def solution(s):
    answer = True
    
    temp = deque()
    for i in s:
        if i == '(':
            temp.append(i)
        
        if i==')' and not temp:
            return False
        elif i==')' and temp:
            temp.popleft()
        
        
        # print(temp , i)
    if temp:
        return False    
    
    return True