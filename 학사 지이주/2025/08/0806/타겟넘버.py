def solution(numbers, target):
    answer = 0
    return dfs(numbers,target,0,0)

def dfs(numbers , target , idx ,now):
    if len(numbers) == idx:
        if target == now:
            return 1
        else:
            return 0
        
    return dfs(numbers,target,idx+1,now+numbers[idx]) + dfs(numbers,target,idx+1 , now-numbers[idx])
