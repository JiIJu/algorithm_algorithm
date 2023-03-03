# 모음사전
from itertools import product

def solution(word):
    answer = [] 
    alpa = ['A','E','I','O','U']
    for i in range(1,6):
        data = list(product(alpa,repeat=i))
        # print(data)
        for j in data:
            answer.append(''.join(j))
    answer = sorted(answer)
    return answer.index(word)+1
