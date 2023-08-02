# swea 1230 암호문3
from collections import deque
for tc in range(1,11):
    N = int(input())
    original = deque(list(map(int,input().split())))
    n = int(input())
    order = list(input().split())
    check = []
    for i in range(n):
        if not order[i].isdigit():
            check.append(i)
    cal = []
    temp = []
    # print(order)
    for i in order:
        if not i.isdigit():
            cal.append(temp)
            temp = [i]
        else:
            temp.append(i)
    cal.pop(0)
    for i in cal:
        n = len(original)
        temp_original = deque([])
        if i[0]=='I':
            x,y,s = int(i[1]),int(i[2]),deque(i[3:])
            for j in range(x):
                temp_original.append(original.popleft())
            for j in range(y):
                temp_original.append(s.popleft())
            while original:
                temp_original.append(original.popleft())
        else:
            if i[0]=='D':
                y,z= int(i[1]),int(i[2])
                for j in range(y):
                    temp_original.append(original.popleft())
                for j in range(z):
                    original.popleft()
                while original:
                    temp_original.append(original.popleft())

            elif i[0] == 'A':
                y,z = int(i[1]),deque(i[2:])
                for j in range(n):
                    temp_original.append(original.popleft())
                for j in range(y):
                    temp_original.append(z.popleft())
        original = temp_original
    print(f'#{tc} ',end='')
    for i in range(10):
        print(original[i],end=' ')
    print()



