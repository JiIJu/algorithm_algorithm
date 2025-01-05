def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    temp = n+1
    check = False
    while not check:
        if cnt == bin(temp).count('1'):
            return temp
        temp+=1