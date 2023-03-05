# 프로그래머스 가장큰수
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers = sorted(numbers , key = lambda x:x*3 , reverse=True)
    numbers = str(int(''.join(numbers)))
    return numbers
