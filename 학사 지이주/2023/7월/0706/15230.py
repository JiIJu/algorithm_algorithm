# swea 15230 알파벳공부
T = int(input())
for tc in range(1,T+1):
  data = input()
  maxv=0
  for i in range(len(data)):
    if i == 0 and data[i]=='a':
      temp = ord(data[0])
      maxv = 1
      check =1
      continue
    elif i==0 and data[i]!='a':
      break
    if ord(data[i])-temp==1:
      temp = ord(data[i])
      check+=1
      if check>maxv:
        maxv = check
    else:
      break
  print(f'#{tc} {maxv}')
