# swea 17319 연속문자열
T = int(input())
for tc in range(1,T+1):
  N = int(input())
  S = input()
  n = len(S)
  if n%2:
    print(f'#{tc} No')
  else:
    temp = n//2
    a = S[:temp]
    a = a+a
    if a==S:
      print(f'#{tc} Yes')
    else:
      print(f'#{tc} No')
