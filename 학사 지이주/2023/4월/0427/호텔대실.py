import heapq
def conv(a):
    return int(a[:2])*60+int(a[3:])
def solution(book_time):
    heap = []
    ans = [-10]
    for i in book_time:
        heapq.heappush(heap,(conv(i[0]),conv(i[1])))
    while heap:
        s,f = heapq.heappop(heap)
        if s >= ans[0]+10:
            heapq.heappop(ans)
            heapq.heappush(ans,f)
        else:
            heapq.heappush(ans,f)
    return len(ans)
            