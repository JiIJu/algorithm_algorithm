def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        if i == 1:
            answer.append(0)
        else:
            k = 1
            for j in range(2,int(i**0.5)+1):
                if not i%j:
                    k = j
                    if i//j<=10000000:
                        k = i//j
                        break
            answer.append(k)
    return answer
