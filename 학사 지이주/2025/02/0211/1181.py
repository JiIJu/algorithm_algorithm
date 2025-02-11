# https://www.acmicpc.net/problem/1181
import sys
N = int(input())
data = [(sys.stdin.readline().rstrip()) for i in range(N)]
data = list(set(data))
data.sort(key=lambda x:(len(x),x))
for i in data:
    print(i)