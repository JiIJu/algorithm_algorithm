# 톱니바퀴
import sys
import copy
from collections import deque
data = [deque(list(input())) for _ in range(4)]

K = int(input())

spin = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]

def left(num,dir):
    if num<0:
        return
    if data[num][2]!=data[num+1][6]:
        left(num-1,-dir)
        data[num].rotate(dir)
def right(num,dir):
    if num>3:
        return
    if data[num][6] != data[num-1][2]:
        right(num+1,-dir)
        data[num].rotate(dir)
for num,dir in spin:
    num-=1
    left(num-1,-dir)
    right(num+1,-dir)
    data[num].rotate(dir)
ans = 0
if data[0][0]=='1':
    ans+=1
if data[1][0]=='1':
    ans+=2
if data[2][0]=='1':
    ans+=4
if data[3][0]=='1':
    ans+=8
print(ans)