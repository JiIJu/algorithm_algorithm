from collections import deque

n = int(input())
data = deque([])

for i in range(n):
    data2 = input().split()
    a = data2[0]
    if len(data2)>1:
        b = data2[1]
    if a == 'push':
        data.append(b)
    elif a == 'pop':
        if len(data):
            print(data.popleft())
        else:
            print(-1)
    elif a =='size':
        print(len(data))
    elif a=='empty':
        if len(data):
            print(0)
        else:
            print(1)
    elif a=='front':
        if len(data):
            print(data[0])
        else:
            print(-1)
    elif a== 'back':
        if len(data):
            print(data[-1])
        else:
            print(-1)