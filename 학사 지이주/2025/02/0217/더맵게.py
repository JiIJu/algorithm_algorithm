# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville)>=2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+2*b)
        
        answer+=1
    if min(scoville)>=K:
        return answer
    else:
        return -1