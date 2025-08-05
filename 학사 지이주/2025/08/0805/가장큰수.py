def solution(numbers):
    answer = ''
    numbers = sorted(numbers , key = lambda x : str(x)*3, reverse = True)
    for i in numbers:
        answer += str(int(i))
    return str(int(answer))

