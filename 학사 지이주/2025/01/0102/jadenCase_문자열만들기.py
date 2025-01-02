def solution(s):
    answer = ''
    temp = True
    for i in s:
        if i == ' ':
            answer += i
            temp = True
            
        elif temp:
            answer+=i.upper()
            temp = False
            
        else:
            answer+=i.lower()
            
    return answer