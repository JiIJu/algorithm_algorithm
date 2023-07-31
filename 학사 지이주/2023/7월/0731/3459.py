# swea 3459 승자예측하기

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = -1
    # N//=2
    # N+=1
    while N>1:
        if temp == -1:
            N//=2
        else:
            N = (N+1)//2
        temp *= -1
    if temp == -1:
        print(f'#{tc} Bob')
    else:
        print(f'#{tc} Alice')