# swea 1244 최대상금
T = int(input())
for tc in range(1,T+1):
  data , c = input().split()
  N = len(data)
  c = int(c)
  now = set([data])
  next = set()
  for _ in range(c):
    while now:
      s = now.pop()
      s = list(s)
      for i in range(N):
        for j in range(i+1,N):
          s[i],s[j] = s[j],s[i]
          next.add(''.join(s))
          s[i],s[j] = s[j],s[i]
    now,next = next,now
  print(f'#{tc} {max(now)}')
