import sys
from collections import deque

C = int(input())
for i in range(C):
    data = deque(list(map(int,input().split())))
    n = data.popleft()
    avg = sum(data)/n
    cnt = 0
    for i in range(len(data)):
        if data[i] > avg:
            cnt+=1

    print(f'{cnt/n*100:.3f}%')

