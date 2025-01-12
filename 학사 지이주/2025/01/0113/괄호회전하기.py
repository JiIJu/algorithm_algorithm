from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    if len(s)==1:
        return 0
    for i in range(len(s)):
        s.append(s.popleft())
        temp = deque([])
        # print(s[0])
        for j in s:
            check = 1
            if not temp and (j==']' or j==')' or j=='}'):
                check = 0
                break
            if j=='(' or j=='{' or j=='[':
                temp.append(j)
            else:
                if not temp:
                    check=0
                    break
                if j ==']':
                    if temp[-1] == '[':
                        temp.pop()
                    else:
                        check=0
                        break
                if j ==')':
                    if temp[-1] == '(':
                        temp.pop()
                    else:
                        check=0
                        break
                if j =='}':
                    if temp[-1] == '{':
                        temp.pop()
                    else:
                        check=0
                        break
        if check and len(temp)==0:
             answer+=1
                         
        
    # for i in s:
        
    return answer