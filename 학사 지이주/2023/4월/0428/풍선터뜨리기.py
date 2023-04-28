def solution(a):
    answer = 0
    n = len(a)
    left = [0] * n
    right = [0] * n
    left[0] = a[0]
    for i in range(1,n):
        left[i] = min(left[i-1],a[i])
    right[-1] = a[-1]
    for i in range(n-2,-1,-1):
        right[i] = min(right[i+1],a[i])
    for i in range(n):
        temp = 0
        if left[i]<a[i]:
            temp+=1
        if right[i]<a[i]:
            temp+=1
        if temp<=1:
            answer+=1
    return answer
