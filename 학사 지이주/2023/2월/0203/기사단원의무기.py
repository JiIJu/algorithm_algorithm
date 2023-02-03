# 프로그래머스 기사단원의 무기
nums = [2]*100001
nums[1]=1
for i in range(2,100001):
    for j in range(2,100001):
        if i*j<=100000:
            nums[i*j] += 1
        else:   
            break
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        if nums[i]<=limit:
            answer+=nums[i]
        else:
            answer+=power
    return answer
