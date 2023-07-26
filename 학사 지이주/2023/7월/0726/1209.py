# swea 1209 sum

for tc in range(1,11):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    ans = []
    maxv=0
    temp3 = 0
    temp4 = 0
    for i in range(100):
        temp1 = 0
        temp2 = 0
        temp3+=data[i][i]
        temp4+=data[99-i][i]
        for j in range(100):
            temp1+=data[i][j]
            temp2+=data[j][i]
        maxv = max(maxv,temp1,temp2,temp3,temp4)
    print(f'#{tc} {maxv}')
