## 11653 소인수분해


n = int(input())

data = []
temp = 2
while n>1:
    if n%temp == 0:
        n = n//temp
        data.append(temp)
    else:
        temp+=1
data.sort()
for i in data:
    print(i)