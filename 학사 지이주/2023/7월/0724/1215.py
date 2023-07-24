# swea 1215 회문1

for tc in range(1,11):
    n = int(input())
    data = [list(input()) for _ in range(8)]
    ans = 0
    for i in range(8):
        for j in range(8-n+1):
            a = data[i][j:j+n]
            if a == a[::-1]:
                ans+=1
    for i in range(8):
        for j in range(8-n+1):
            b = ''
            for k in range(n):
                b+=data[j+k][i]
            if b == b[::-1]:
                ans+=1
    print(f'#{tc} {ans}')