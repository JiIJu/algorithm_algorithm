# 프로그래머스 124나라의숫자
def solution(n):
    answer = ''
    temp = ''
    i = 1
    while n>0:
        if n%3 == 0:
            temp +='4'
            n = n//3-1
            continue
        elif n%3 == 1:
            temp += '1'
        else:
            temp +='2'
        n = n // 3
    print(temp)
    return temp[::-1]
