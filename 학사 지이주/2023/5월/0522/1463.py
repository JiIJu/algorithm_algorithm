# 1463 1로만들기

N = int(input())
num = [9999999]*(10**6+1)
num[1]=0
num[2] = 1
num[3] = 1
num[4] = 2

for i in range(5,N+1):
    if not i%2:
        num[i] = min(num[i],num[i//2]+1)
    if not i%3:
        num[i] = min(num[i],num[i//3]+1)
    num[i] = min(num[i],num[i-1]+1)
print(num[N])
