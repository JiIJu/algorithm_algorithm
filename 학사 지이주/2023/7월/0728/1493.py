# swea 1493 수의 새로운 연산
def fib(n):
    if n<2:
        check[n] = 1
    else:
        check[n] = check[n-1] + n
data = [[0] * 301 for _ in range(301)]
ans = [0]*100001
check = [0]*301
for i in range(1,301):
    fib(i)

for i in range(1,301):
    temp = i
    data[i][1] = check[i]
    if data[i][1]<=100000:
        ans[data[i][1]] = [i,1]
    for j in range(2,301):
        if data[i][j-1] + temp >= 100000:
            break
        data[i][j] = data[i][j-1] + temp

        ans[data[i][j]] = [i,j]
        temp+=1
T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input().split())
    # temp2 = [ans[a][0]+ans[b][0],ans[a][1]+ans[b][1]]
    for i in range(len(ans)):
        if ans[i] == [ans[a][0]+ans[b][0],ans[a][1]+ans[b][1]]:
            print(f'#{tc} {i}')
            break