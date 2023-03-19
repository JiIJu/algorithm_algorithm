import heapq
def solution(operations):
    answer = []
    data = []
    for i in operations:
        a,b = i.split()
        b = int(b)
        data.append([a,b])
    maxv = 0
    minv = 9999999
    temp = []
    for order,num in data:
        if order == 'I':
            heapq.heappush(temp,(-num,num))
        elif temp and order == 'D' and num == -1:
            temp = sorted(temp, key=lambda x:x[1])
            heapq.heappop(temp)
        elif temp and order == 'D' and num == 1:
            heapq.heappop(temp)
    if not temp:
        return [0,0]
    else:
        for a,b in temp:
            maxv = max(maxv,b)
            minv = min(minv,b)
        return [maxv,minv]