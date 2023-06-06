# 11053 가장 긴 증가하는 부분 수열

n = int(input())
data = list(map(int,input().split()))
ans = [1]*n
# ans[0] = 1
for i in range(1,n):
    for j in range(i):
        if data[i]>data[j]:
            ans[i] = max(ans[i],ans[j]+1)

print(max(ans))