# swea 1231 중위순회
def order(n):
  if n:
    order(left[n])
    print(text[n],end='')
    order(right[n])

for tc in range(1,11):
  N = int(input())
  left = [0]*(N+1)
  right = [0]*(N+1)
  text = [0]*(N+1)

  for i in range(N):
    data = list(input().split())
    if len(data)==4:
      text[int(data[0])] = data[1]
      left[int(data[0])] = int(data[2])
      right[int(data[0])] = int(data[3])
    elif len(data)==3:
      text[int(data[0])] = data[1]
      left[int(data[0])] = int(data[2])
    else:
      text[int(data[0])] = data[1]
  print(f'#{tc}',end=' ')
  order(1)
  print()
