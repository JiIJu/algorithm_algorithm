# https://www.acmicpc.net/problem/1251

data = list(input())
n = len(data)
temp = []
a = ''
b = ''
c = ''
for i in range(n-2):
    for q in data[:i+1]:
        # print(q,i)
        a+=q
    for j in range(i+1,n-1):
        b += data[j]
        for k in range(j+1,n):
            c += data[k]
        temp.append([a[::-1],b[::-1],c[::-1]])
        c = ''
    b = ''
    a = ''
    
    
# print(temp)
temp = sorted(temp)
# print(temp)
print(''.join(temp[0]))