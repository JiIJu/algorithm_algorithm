def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    while left<=right:
        cnt = 0
        mid = (left+right)//2
        for i in times:
            cnt += (mid//i)
            if cnt>=n:
                break
        if cnt>=n:
            answer = mid
            right = mid-1
        else:
            left = mid+1

    return answer