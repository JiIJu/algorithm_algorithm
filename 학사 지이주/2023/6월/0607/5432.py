# 5432 스티커
import sys
T = int(input())
for tc in range(T):
    n = int(input())
    ans= [list(map(int,sys.stdin.readline().split())) for _ in range(2)]

    for i in range(1,n):
        if i == 1:
            ans[0][i] += ans[1][i-1]
            ans[1][i] += ans[0][i-1]
        else:
            ans[0][i] += max(ans[1][i-1] , ans[1][i-2])
            ans[1][i] += max(ans[0][i - 1] , ans[0][i-2])
    print(max(ans[0][-1],ans[1][-1]))