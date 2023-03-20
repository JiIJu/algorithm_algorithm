import heapq
def solution(n, works):
    answer = 0
    data = []
    for i in works:
        heapq.heappush(data,(-i,i))
    while n>0:
        a,b = heapq.heappop(data)
        b -=1
        heapq.heappush(data,(-b,b))
        n-=1
    for a,b in data:
        if b<0:
            continue
        answer += b*b
    return answer
