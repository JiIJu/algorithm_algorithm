import heapq

def solution(A,B):
    answer = 0
    n = len(A)
    new_B = []
    heapq.heapify(A)
    for i in range(n):
        heapq.heappush(new_B,(-B[i],B[i]))
                       
    for i in range(n):
        answer += heapq.heappop(A)*heapq.heappop(new_B)[1]
    return answer