# SWEA 2806 N-QUEEN
def check(x):
  for i in range(x):
    if data[i]==data[x] or abs(data[i]-data[x]) == abs(i-x):
      return 0
  return 1
def dfs(x):
  global result
  if x==N:
    result +=1
  else:
    for i in range(N):
      data[x] = i
      if check(x):
        dfs(x+1)
T = int(input())
for tc in range(1,T+1):
  N = int(input())
  data = [0]*N
  result = 0 
  dfs(0)
  print(f'#{tc} {result}')
