def solution(storey):
    answer = 0
    while storey > 0:
        a = storey % 10
        if a >5:
            answer += 10 -a
            storey += 10
        elif a<5:
            answer += a
        else:
            if (storey//10)%10 >= 5:
                answer += 5
                storey += 10
            else:
                answer += 5
        storey = storey//10
    return answer