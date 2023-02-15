def solution(s):
    from collections import deque
    answer = 0
    for i in range(len(s)):
        temp = deque(s)
        for j in range(i):
            temp.append(temp.popleft())
        stack = []
        check = 1
        for j in temp:
            if j == '[' or j == '{' or j == '(':
                stack.append(j)
            elif stack and j==']' and stack[-1] == '[':
                stack.pop()
            elif stack and j == ')' and stack[-1] =='(':
                stack.pop()      
            elif stack and j == '}' and stack[-1] =='{':
                stack.pop()
            else:
                check = 0
                break
        if check and len(stack)==0:
            answer+=1
    return answer
