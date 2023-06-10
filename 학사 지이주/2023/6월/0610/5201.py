# 5201 N과M (12)


N,M = map(int,input().split())
data = sorted(set(map(int,input().split())))
ans = []
def solve(n):
    if n==M:
        print(*ans)
        return
    for i in range(len(data)):
        if n==0 or ans[-1]<=data[i]:
            ans.append(data[i])
            solve(n+1)
            ans.pop()
solve(0)
