# 프로그래머스 [3차] n진수 게임
def change(n,num):
    ans = ''
    if num==0:
        return '0'
    while num>0:
        check = num%n
        if check>=10:
            if check==10:
                ans += 'A'    
            elif check == 11:
                ans += 'B'
            elif check == 12:
                ans+='C'
            elif check == 13:
                ans += 'D'
            elif check == 14:
                ans += 'E'
            elif check == 15:
                ans += 'F'
        else:
            ans += str(num%n)
        num = num//n
    return ans[::-1]
def solution(n, t, m, p):
    answer = ''
    tube = []
    temp = p-1
    for i in range(t):
        tube.append(temp)
        temp += m
    check = []
    for i in range(1000001):
        temp = change(n,i)
        for j in temp:
            check.append(j)
    for i in tube:
        answer+=check[i]
    return answer
