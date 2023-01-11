# 5397 키로거

from collections import deque

T = int(input())

for tc in range(T):
    data = input()
    q = []
    w = []
    for i in data:
        if i=='<':
            if q:
                w.append(q.pop())
        elif i=='>':
            if w:
                q.append(w.pop())
        elif i=='-':
            if q:
                q.pop()
        else:
            q.append(i)
    print(''.join(q)+''.join(reversed(w)))
