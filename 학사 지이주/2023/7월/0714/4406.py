#swea 4406 모음이 보이지 않는 사람
T = int(input())
for tc in range(1,T+1):
  data = input()
  print(f'#{tc}',end=' ')
  for i in data:
    if i not in ('a','e','i','o','u'):
      print(i,end='')
  print()
