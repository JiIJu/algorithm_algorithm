from collections import deque
def solution(n, wires):
    answer = -1
    
    
    data = [[] for _ in range(n+1)]
    
    for i,j in wires:
        data[i].append(j)
        data[j].append(i)
    
    def bfs(start,cut1,cut2):
        check = [False] * (n+1)
        check[start] = True
        
        q = deque([start])
        cnt=1
        while q:
            now = q.popleft()
            for i in data[now]:
                if (i == cut1 and now == cut2) or (i == cut2 and now == cut1):
                    continue
                if check[i] == False:
                    check[i]= True
                    cnt +=1
                    q.append(i)
        return cnt
    maxv = 99999
    for i,j in wires:
        ans = bfs(i,i,j)
        maxv = min(maxv,abs(n-2*ans))
    
    
    return maxv