# 1991 트리순회
def pre(a):
    if a!='.':
        print(a,end='')
        pre(data[a][0])
        pre(data[a][1])

def pre2(a):
    if a!='.':
        pre2(data[a][0])
        print(a, end='')
        pre2(data[a][1])

def pre3(a):
    if a!='.':
        pre3(data[a][0])
        pre3(data[a][1])
        print(a, end='')
N = int(input())
data = {}

for i in range(N):
    root,left,right = input().split()
    data[root] = [left,right]

pre('A')
print()
pre2('A')
print()
pre3('A')