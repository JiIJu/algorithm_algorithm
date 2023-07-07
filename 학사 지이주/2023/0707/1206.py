# swea 1206 View

for tc in range(1,11):
  N = int(input())
  ans = 0
  data = list(map(int,input().split()))
  for i in range(2,N-2):
    temp = data[i]
    maxv = max(data[i-2],data[i-1],data[i+1],data[i+2])
    if temp-maxv>0:
      ans+= temp-maxv
  print(f'#{tc} {ans}')
