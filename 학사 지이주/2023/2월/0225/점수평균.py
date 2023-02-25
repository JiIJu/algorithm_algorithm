#hmat 점수평균
import sys

N,K = map(int,input().split())
score = list(map(int,input().split()))
ans_list = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]

for a,b in ans_list:
    temp = sum(score[a-1:b])
    print(f"{(temp/(b-a+1)):.2f}")
