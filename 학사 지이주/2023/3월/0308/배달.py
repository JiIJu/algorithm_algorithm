# 프로그래머스 배달
import heapq
def solution(N, road, K):
    global data,answer
    answer = 0
    INF = float('inf')
    distance = [INF]*(N+1)
    distance[1]=0
    data = [[] for _ in range(N+1)]
    for a,b,c in road:
        data[a].append([c,b])
        data[b].append([c,a])
    def dijkstra(distance,data):
        heap = []
        heapq.heappush(heap,[0,1])
        while heap:
            cost,node = heapq.heappop(heap)
            for c,n in data[node]:
                if cost + c < distance[n]:
                    distance[n] = cost+c
                    heapq.heappush(heap,[cost+c,n])
                    
                    
    dijkstra(distance,data)
    for i in range(1,len(distance)):
        if distance[i]<=K:
            answer+=1
    print(distance)
    return answer
