# swea 16800 구구단걷기
T = int(input())
for tc in range(1,T+1):
  N = int(input())
  data = []
  for i in range(1,int(N**0.5)+1):
    if not N%i:
      data.append(i)
  print(f'#{tc} {N//max(data)+max(data)-2}')
