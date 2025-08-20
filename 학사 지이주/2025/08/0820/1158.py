## 1158 요시푸스 문제
from collections import deque
n,m = map(int,input().split())

data = deque([i for i in range(1,n+1)])

check = 1

ans = []

while data:
    if m == check:
        ans.append(data.popleft())
        check = 1
    else:
        check +=1
        data.append(data.popleft())
print('<',end='')
a = len(ans)
for i in range(a):
    if i != a-1:
        print(ans[i],end=', ')
    else:
        print(ans[i],end='')
print('>')

