# swea 17299 최소 덧셈
T = int(input())
for tc in range(1,T+1):
  N = input()
  minv = 9999999
  for i in range(len(N)-1):
    a,b = N[:i+1] , N[i+1:]
    print(a,b)
    minv = min(int(a)+int(b),minv)
  print(f'#{tc} {minv}')
