# swea 2817 부분수열합

from itertools import combinations
T = int(input())
for tc in range(1,T+1):
    N , K = map(int,input().split())
    data = list(map(int,input().split()))
    visit = [0]*(sum(data)+1)
    check = [0]
    for i in range(len(data)):
        for j in range(len(check)):
            visit[check[j]+data[i]] +=1
            check.append(check[j]+data[i])
    print(f'#{tc} {visit[K]}')