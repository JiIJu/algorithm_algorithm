# swea 정곤이의 단조 증가하는 수
from itertools import permutations
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    new_data = list(permutations(data,2))
    maxv = 0
    for a,b in new_data:
        new_num = a*b
        strnew_num = str(new_num)
        check = 1
        for i in range(len(strnew_num)-1):
            if strnew_num[i+1] < strnew_num[i]:
                check = 0
                break
        if check:
            maxv = max(maxv,new_num)
    if maxv:
        print(f'#{tc} {maxv}')
    else:
        print(f'#{tc} -1')