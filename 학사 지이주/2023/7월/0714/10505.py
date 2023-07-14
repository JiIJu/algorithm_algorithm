# swea 10505 소득불균형
T = int(input())
for tc in range(1,T+1):
  N = int(input())
  data = list(map(int,input().split()))
  ans = 0
  check = sum(data)/len(data)
  for i in data:
    if i <= check:
      ans+=1
  print(f'#{tc} {ans}')
