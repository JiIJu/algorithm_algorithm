from itertools import permutations
def solution(numbers):
    answer = 0
    data = {}
    n = len(numbers)
    
    for i in range(1,n+1):
        temp = list(permutations(numbers,i))
        for j in temp:
            a = int(''.join(j))
            if a not in data:
                data[a] = 1
    for i in data:
        if i > 1:
            answer += check(i)
    return answer


def check(n):
    
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
