# 프로그래머스 JadenCase문자열만들기.py
def solution(s):
    answer = ''
    data = list(s)
    check = 1
    for i in s:
        if i == ' ':
            check=1
            answer+=i
        elif check==1 and 'a'<=i<='z':
            answer+=i.upper()
            check=0
        elif check==0 and 'A'<=i<='Z':
            answer+=i.lower()
            check=0
        else:
            answer+=i
            check=0
        
    return answer
