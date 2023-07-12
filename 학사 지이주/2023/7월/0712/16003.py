# swea 16003 화면캡쳐
def dfs(n,depth):
  global count
  if count >=50:
    return
  if depth>=max_depth:
    return
  if int(n)<=N:
    count +=1
    ans.append(n+'.png')
  for i in range(10):
    dfs(n+str(i),depth+1)
T = int(input())
for tc in range(1,T+1):
  N = input().rstrip()
  max_depth = len(N)
  count = 0
  N = int(N)
  ans = []
  print(f'#{tc} ',end='')
  for i in range(1,10):
    dfs(str(i),0)
  print(*ans)
