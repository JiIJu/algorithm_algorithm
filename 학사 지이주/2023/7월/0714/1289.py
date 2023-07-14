# swea 1289. 원재의 메모리 복구하기
T = int(input())
for tc in range(1,T+1):
  data = input() 
  ans = 0
  check = int(data[0])
  if int(check):
    ans+=1
  for i in range(1,len(data)):
    if int(data[i]) != check:
      check = int(data[i])
      ans+=1
  print(f'#{tc} {ans}')
