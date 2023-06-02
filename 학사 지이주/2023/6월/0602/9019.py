# 9019 DSLR
import sys
from collections import deque

def bfs(a,b):
    q = deque([[a,'']])
    visit[a]=1
    while q:
        now,word = q.popleft()
        if now == b:
            return ''.join(word)
        for d in range(4):
            if d==0:
                if now*2>9999:
                    if not visit[(2*now)%10000]:
                        q.append([(2*now)%10000,word+'D'])
                        visit[(2*now)%10000]=1
                else:
                    if not visit[now*2]:
                        q.append([now*2,word+'D'])
                        visit[now*2]=1
            elif d==1:
                if now==0:
                    if not visit[9999]:
                        q.append([9999,word+'S'])
                        visit[9999]=1
                else:
                    if not visit[now-1]:
                        q.append([now-1,word+'S'])
                        visit[now-1]=1
            elif d==2:
                if not visit[now//1000+(now%1000)*10]:
                    q.append([now//1000+(now%1000)*10,word+'L'])
                    visit[now//1000+(now%1000)*10]=1
            elif d==3:
                if not visit[now//10+(now%10)*1000]:
                    q.append([now//10+(now%10)*1000,word+'R'])
                    visit[now//10+(now%10)*1000]=1
T = int(input())
for tc in range(T):
    A,B = map(int,sys.stdin.readline().split())
    visit = [0]*10001

    print(bfs(A,B))
