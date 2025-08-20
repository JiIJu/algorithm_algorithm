# 10798 세로읽기

data = []
line = []
maxv = 0
for i in range(5):
    a = list(input())
    data.append(a)
    maxv = max(maxv,len(a))

ans = ''
temp = 0
for j in range(maxv):
    for i in range(5):
        if len(data[i])>temp:
            ans+=data[i][temp]
    temp+=1
print(ans)