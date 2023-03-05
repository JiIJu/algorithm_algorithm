def isprime(n):
    if n<=1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
from itertools import permutations
def solution(numbers):
    answer = []
    numbers = list(numbers)
    
    for i in range(1,len(numbers)+1):
        data = list(permutations(numbers,i))
        for j in data:
            if isprime(int(''.join(j))):
                answer.append(int(''.join(j)))
    return len(set(answer))
