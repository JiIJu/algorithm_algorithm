#프로그래머스 약수의개수와덧셈
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        temp = 1
        cnt=1
        while temp<i//2+1:
            if i%temp==0:
                cnt+=1
            temp+=1
        if cnt%2:
            answer-=i
        else:
            answer+=i
    
    return answer
