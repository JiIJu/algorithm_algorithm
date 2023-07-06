# swea 16910 원안의점
import math
T = int(input())
for tc in range(1,T+1):
  N = int(input())
  ans = 0
  for i in range(1,N):
    ans+=math.trunc(((N**2-i**2)**0.5))
  ans = ans*4 + 4*N+1
  print(f'#{tc} {ans}')
