import heapq
def solution(A, B):
    answer = 0

    heapq.heapify(A)
    heapq.heapify(B)
    while A and B:
        a,b = heapq.heappop(A),heapq.heappop(B)
        if a<b:
            answer +=1
        elif a>=b:
            heapq.heappush(A,a)

    return answer
