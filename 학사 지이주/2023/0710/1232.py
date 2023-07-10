# swea 1232 사칙연산
def post_order(n):
  if n:
    post_order(left[n])
    post_order(right[n])
    if order[n] == '+':
      order[n] = int(order[left[n]]) + int(order[right[n]])
    elif order[n] == '-':
      order[n] = int(order[left[n]]) - int(order[right[n]])
    elif order[n] == '*':
      order[n] = int(order[left[n]]) * int(order[right[n]])
    elif order[n] == '/':
      order[n] = int(order[left[n]]) // int(order[right[n]])
for tc in range(1,11):
  N = int(input())
  left = [0]*(N+1)
  right = [0]*(N+1)
  order = [0]*(N+1)
  for i in range(N):
    data = list(input().split())
    order[int(data[0])] = data[1]
    if len(data)==4:
      left[i+1] = int(data[2])
      right[i+1] = int(data[3])
  post_order(1)
  print(f'#{tc} {order[1]}')
