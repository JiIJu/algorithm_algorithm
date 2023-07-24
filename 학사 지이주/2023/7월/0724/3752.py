# swea 3752 가능한 시험 점수
from itertools import combinations
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    visit = [1] + [0]*sum(data)
    check = [0]
    for i in range(len(data)):
        for j in range(len(check)):
            if not visit[check[j]+data[i]]:
                visit[check[j]+data[i]] = 1
                check.append(check[j]+data[i])
    print(f'#{tc} {sum(visit)}')