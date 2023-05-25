# 9095 1,2,3더하기
import sys
T = int(input())

for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    num = [0] * 11
    num[1] = 1
    num[2] = 2
    num[3] = 4
    for i in range(4,11):
        num[i] = num[i-1] + num[i-2] + num[i-3]
    print(num[N])