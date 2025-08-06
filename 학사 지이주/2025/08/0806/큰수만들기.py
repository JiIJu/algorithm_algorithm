from collections import deque
def solution(number, k):
    answer = ''
    stack = deque([])
    check = k
    idx = 0
    for i in range(len(number)):
        temp = 0
        while stack and check > 0 and stack[-1] < number[i]:
            stack.pop()
            check -= 1
        stack.append(number[i])
    while len(stack)>len(number)-k:
        stack.pop()

    return ''.join(stack)




# from itertools import combinations
# def solution(number, k):
#     answer = '0'
#     number = list(number)
#     temp = list(combinations(number,len(number)-k))
#     for i in temp:
#         a = (''.join(i))
#         if int(a)>int(answer):
#             answer = a
#     return answer


# import sys
# sys.setrecursionlimit(10**6) 
# def solution(number, k):
#     global temp
#     answer = ''
#     data = []
#     temp = []
#     number = list(number)
#     dfs(number,k,0,0,'')

#     return str(max(temp))


# def dfs(number,k,idx,check,now):
#     if len(number)-k == check:
#         temp.append(int(now))
#         return 0
#     if idx>=len(number):
#         return 0
#     return dfs(number,k,idx+1,check,now) + dfs(number,k,idx+1,check+1,now+number[idx])
