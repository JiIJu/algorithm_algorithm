## 10828 
import sys
from collections import deque
n = int(input())

a = [sys.stdin.readline().strip() for _ in range(n)]

stack = deque([])

for i in a:
    temp = i.split()
    if len(temp) == 2:
        stack.append(temp[1])
    else:
        if temp[0]=='pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif temp[0]=='size':
            print(len(stack))
        elif temp[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif temp[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

        