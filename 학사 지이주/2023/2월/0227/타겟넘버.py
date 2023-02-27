from collections import deque
def solution(numbers, target):
    global ans
    ans = 0
    numbers = deque(numbers)
    dx = [1,-1]
    def dfs(idx,numbers,num):
        global ans
        if idx==len(numbers) and num==target:
            ans+=1
            return
        if idx == len(numbers):
            return
        dfs(idx+1,numbers,num+numbers[idx])
        dfs(idx+1,numbers,num-numbers[idx])
    dfs(0,numbers,0)
        
    return ans
