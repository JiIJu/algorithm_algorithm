# 1541 잃어버린 괄호

data = list(input().split('-'))
ans = 0
for i in data[0].split('+'):
    ans += int(i)

for i in range(1,len(data)):
    num = data[i].split('+')
    for j in num:
        ans -= int(j)
print(ans)
