# swea 1222 계산기1
for tc in range(1,11):
  n = int(input())
  data = input().split('+')
  ans = 0
  for i in data:
    ans+=int(i)
  print(f'#{tc} {ans}')
