def dfs(numbers,target,idx,sum_num):
    if idx == len(numbers):
        if sum_num == target:
            return 1
        else:
            return 0
    return dfs(numbers,target,idx+1,sum_num+numbers[idx]) +dfs(numbers,target,idx+1,sum_num-numbers[idx])
def solution(numbers, target):
    answer = 0
    return dfs(numbers,target,0,0)