# 프로그래멋 다음에 나올 숫자
def solution(common):
    answer = 0
    n = len(common)
    check = 0
    if 0 in common:
        gap = common[1]-common[0]
        check = 1
    else:
        a = common[1]
        gap = common[1]-common[0]
        mul = common[1]/common[0]
        if common[2]-a != gap:
            check=2
        elif common[2]/a !=mul:
            check=1
    if check==1:
        answer = (gap+common[-1])
    else:
        answer = mul*common[-1]
    return answer
