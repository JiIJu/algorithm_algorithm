# 18870 좌표압축

N = int(input())
data = list(map(int,input().split()))
ans = sorted(set(data))
check = {ans[i]:i for i in range(len(ans))}
for i in data:
    print(check[i],end=' ')