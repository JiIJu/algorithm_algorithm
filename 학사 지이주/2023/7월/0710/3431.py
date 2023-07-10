# swea 3431 준환이의 운동관리
T = int(input())
for tc in range(1,T+1):
  a,b,c = map(int,input().split())
  if c>b:
    print(f'#{tc} -1')
  elif a<=c<=b:
    print(f'#{tc} 0')
  else:
    print(f'#{tc} {a-c}')
