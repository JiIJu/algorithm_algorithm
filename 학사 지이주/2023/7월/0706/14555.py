# swea 14555 공과잡초
from collections import deque
T = int(input())
for tc in range(1,T+1):
  S = input()
  ans = 0
  for i in range(len(S)-1):
    if S[i]=='(' and S[i+1] == '|':
      ans+=1
    elif S[i] == '|' and S[i+1] == ')':
      ans+=1
    elif S[i] == '(' and S[i+1] == ')':
      ans+=1
  print(f'#{tc} {ans}')
      
