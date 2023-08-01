# swea 1228 암호문1
from collections import deque
for tc in range(1,11):
    N = int(input())
    original = deque(list(map(int,input().split())))
    n = int(input())
    order = list(input().split(' I '))
    order[0] = order[0][2:]
    for i in range(len(order)):
        order[i] = order[i].split(' ')
    for i in order:
        new_origin = deque([])
        temp = deque(original)
        a,b,c = int(i[0]),int(i[1]),i[2:]
        c = deque(c[:b])
        for j in range(a):
            new_origin.append(temp.popleft())
        for j in range(b):
            new_origin.append(c.popleft())
        z = len(temp)
        for j in range(z):
            new_origin.append(temp.popleft())
        original = new_origin
    print(f'#{tc} ',end='')
    for i in range(10):
        print(original[i],end=' ')
    print()
