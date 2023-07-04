import sys
N = int(input())
A = []
for i in range(N):
    A.append(int(sys.stdin.readline()))
M = int(input())
B = []
for i in range(M):
    B.append(int(sys.stdin.readline()))
B.sort()
data = []
for i in range(N-M+1):
    data.append(sorted(A[i:i+M]))
ans = []

for i in range(len(data)):
    temp = []
    check = data[i][0]-B[0]
    a = 1
    for j in range(1,M):
        if check != data[i][j]-B[j]:
            a=0
            break
    if a:

        ans.append(i)
print(len(ans))
for i in ans:
    print(i+1)
