# 14889 스타트와 링크

from itertools import combinations
n = int(input())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

member = [i for i in range(1,n+1)]

check = list(combinations(member,n//2))

minv = 99999999999

for i in check:
    temp = []
    a1 , a2 = 0,0

    for j in member:
        if j not in i:
            temp.append(j)
    for j in range(len(i)-1):
        for k in range(j,len(i)):
            a1+= data[i[j]-1][i[k]-1] + data[i[k]-1][i[j]-1]
    for j in range(len(temp) - 1):
        for k in range(j, len(temp)):
            a2 += data[temp[j]-1][temp[k]-1] + data[temp[k]-1][temp[j]-1]
    # print(a1,a2)
    minv = min(minv,abs(a1-a2))
print(minv)

