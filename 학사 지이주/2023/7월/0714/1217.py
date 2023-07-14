# swea 1217 거듭제곱
def solve(a,b):
  if b:  
    if b%2:
      return solve(a,b//2) * solve(a,b//2) * a
    else:
      return solve(a,b//2) * solve(a,b//2)
  else:
    return 1

for tc in range(1,11):
  n = int(input())
  a,b = map(int,input().split())
  ans = solve(a,b)
  print(f'#{tc} {ans}')
