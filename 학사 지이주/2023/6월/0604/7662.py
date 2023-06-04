# 7662 이중 우선순위 큐
import sys
import heapq
T = int(input())

for tc in range(T):
    k = int(input())
    visit = [0]*k
    maxV,minV = [],[]
    for i in range(k):
        I,n = sys.stdin.readline().split()
        n = int(n)
        if I=='I':
            heapq.heappush(maxV,(-n,i))
            heapq.heappush(minV, (n, i))
            visit[i]=1
        elif I=='D' and n==1:
            while maxV and not visit[maxV[0][1]]:
                heapq.heappop(maxV)
            if maxV:
                visit[maxV[0][1]]=0
                heapq.heappop(maxV)
        elif I=='D' and n==-1:
            while minV and not visit[minV[0][1]]:
                heapq.heappop(minV)
            if minV:
                visit[minV[0][1]]=0
                heapq.heappop(minV)
    while maxV and visit[maxV[0][1]]==0:
        heapq.heappop(maxV)
    while minV and visit[minV[0][1]]==0:
        heapq.heappop(minV)
    if minV and maxV:
        print(-maxV[0][0],minV[0][0])
    else:
        print('EMPTY')