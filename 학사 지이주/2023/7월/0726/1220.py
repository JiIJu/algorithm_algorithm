# swea 1220 Magnetic
# 1 = N 2 = S
from collections import deque
for tc in range(1,11):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        temp = ''
        for j in range(N):
            if data[j][i] != 0:
                temp+=str(data[j][i])
        if len(temp)==1:
            continue
        check = ''
        for i in temp:
            if i =='1' and not check:
                check+=i
            if i=='2' and check == '1':
                ans+=1
                check=''
    print(f'#{tc} {ans}')


