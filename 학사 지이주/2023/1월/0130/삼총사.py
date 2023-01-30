#프로그래머스 삼총사
def solution(number):
    answer = []
    def comb():
        for i in range(1<<len(number)):
            res = []
            for j in range(len(number)):
                if i & (1<<j):
                    res.append(number[j])
            if len(res)==3:
                answer.append(res)
    comb()
    
    a = 0
    for i in answer:
        if sum(i)==0:
            a+=1
    return a
