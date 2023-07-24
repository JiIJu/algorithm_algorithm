# swea 14413 격자판 칠하기
from collections import deque
def bfs(x,y):
  q = deque([(x,y)])
  while q:
    i,j = q.popleft()
    for d in range(4):
      ni = i + di[d]
      nj = j + dj[d]
      if 0<=ni<N and 0<=nj<M:
        if  data[i][j] == '.':
          if data[ni][nj] == '?':
            data[ni][nj] = '#'
            q.append((ni,nj))
          elif data[ni][nj] == '.':
            return False
        if data[i][j] == '#':
          if data[ni][nj] == '?':
            data[ni][nj] = '.'
            q.append((ni,nj))
          elif data[ni][nj] == '#':
            return False
  return True
        
T = int(input())
for tc in range(1,T+1):
  N,M = map(int,input().split())
  data = [list(input()) for _ in range(N)]
    # '#' 검정 . 흰색 ? 아무거나
  check = []
  for i in range(N):
    for j in range(M):
      if data[i][j] != '?':
        check.append((i,j))
  di = [-1,1,0,0]
  dj = [0,0,-1,1]
  a = 1
  for i,j in check:
    if not bfs(i,j):
      a = 0
      break
  if a:
    print(f'#{tc} possible')
  else:
    print(f'#{tc} impossible')
