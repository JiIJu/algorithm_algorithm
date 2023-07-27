# swea 1251 하나로
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
def union(a,b):
    r_a = find(a)
    r_b = find(b)
    if r_a < r_b:
        root[r_b] = r_a
    else:
        root[r_a] = r_b
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    root = [i for i in range(N)]
    data = []
    for i in range(N):
        for j in range(N):
            data.append([(X[i]-X[j])**2 + (Y[i]-Y[j])**2 , i , j])
    data.sort()
    cnt = 0
    result = 0
    for i in range(len(data)):
        if cnt == N-1:
            break
        d,i,j = data[i]
        if find(i) != find(j):
            union(i,j)
            cnt+=1
            result += d
    print(f'#{tc} {int(result*E+0.5)}')