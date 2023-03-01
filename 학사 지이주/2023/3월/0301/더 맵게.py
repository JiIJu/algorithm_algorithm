# 프로그래머스 더 맵게
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0]>=K:
        return 0
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a+b*2
        heapq.heappush(scoville,c)
        answer+=1
    return answer
