# https://www.acmicpc.net/problem/2828

n,m = map(int,input().split())
j = int(input())
apple = []
now = 1
length = m-1
ans = 0
for i in range(j):
    apple.append(int(input()))
temp = 0
for i in apple:
    
    if i < now:
        ans += now-i
        now = i
    elif i > now + (m-1):
        ans = ans + ( i - (now + m - 1) )
        now = i-(m-1)

    
    # print(f'temp : {temp} now : {now}')

print(ans)

