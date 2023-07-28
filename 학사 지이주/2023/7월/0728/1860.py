# swea 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    a = 0
    bread = 0
    temp=0
    for i in sorted(arr):
        a +=1
        bread = (i//M)*K
        bread -= a
        if bread<0:
            temp = 1
            break
    if not temp:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')