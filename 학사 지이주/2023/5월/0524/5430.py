# 5430 AC
from collections import deque
T = int(input())
for tc in range(T):
    p = input()
    n = int(input())
    data = input()
    data = deque(data[1:-1].split(','))
    cnt = 0
    check = 0
    for i in p:
        if i == 'R':
            cnt +=1
        elif i == 'D':
            if len(data):
                if data[0]=='':
                    check=1
                    break
                if cnt%2:
                    data.pop()
                else:
                    data.popleft()
            else:
                check = 1
                break
    if check:
        print('error')
    else:
        if data:
            if cnt%2:
                data.reverse()
            print('[',end='')
            for i in range(len(data)-1):
                print(data[i],end=',')
            print(f'{data[-1]}]')
        else:
            print([])