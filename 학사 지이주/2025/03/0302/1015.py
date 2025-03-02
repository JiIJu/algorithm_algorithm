n = int(input())
data = list(map(int,input().split()))
sorted_data = sorted(data)
temp = [0]*n

for i in range(n):
    for j in range(n):
        if sorted_data[j] == data[i]:
            temp[i] = j
            sorted_data[j] = -1
            break
print(*temp)

