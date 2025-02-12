# https://www.acmicpc.net/problem/1343
from collections import deque
data = input()
q , w = 'AAAA', 'BB'
queue = deque([])
a = ''
for i in data:
    if i !='.':
        a += i
    if i == '.' and len(a)>0:
        queue.append(a)
        queue.append(i)
        a = ''
    elif i =='.':
        queue.append(i)
if data[-1] != '.':
    queue.append(a)
ans = ''
temp = 0
for i in queue:
    if i == '.':
        ans += i
    elif len(i)%2 != 0:
        print(-1)
        temp = 1
        break
    elif len(i)%2==0:
        ans += q*(len(i)//4) + (((len(i)%4))//2)*w
    
if not temp:
    print(ans)