# 2748 피보나치수 2

n = int(input())

data = [0]*(91)

data[1] =1
data[2]=1
data[3]=2
for i in range(4,91):
    data[i] = data[i-2]+data[i-1]
print(data[n])