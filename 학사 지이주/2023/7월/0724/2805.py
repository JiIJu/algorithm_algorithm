# swea 2805 농작물 수확하기
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    data = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            data[i][j] = int(data[i][j])
    check = n // 2
    ans = sum(data[check])

    for i in range(1,check+1):
        ans += sum(data[check-i][i:n-i])
        ans += sum(data[check + i][i:n - i])
    print(f'#{tc} {ans}')
