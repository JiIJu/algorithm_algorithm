# 프로그래머스 할인행사
def solution(want, number, discount):
    answer = 0
    data = {}
    for i in range(len(want)):
        data[want[i]] = number[i]
    print(data)
    N = len(discount)
    for i in range(N-9):
        temp = {}
        check=1
 
        for j in range(10):
            if discount[i+j] not in data:
                check = 0
                break
            if discount[i+j] in temp:
                temp[discount[i+j]] +=1
            else:
                temp[discount[i+j]] =1
        res = 0
        if check:
            for i in data:
                if i not in temp:
                    res = 1
                    break
                if data[i] != temp[i]:
                    res = 1
                    break
        if res==0 and check:
            answer+=1
    return answer
