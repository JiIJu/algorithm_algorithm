# swea 4408 자기 방으로 돌아가기

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    cnt = [0]*201
    for a,b in data:
        if b<a:
            s = (b+1)//2
            e = (a+1)//2
        else:
            s = (a + 1) // 2
            e = (b + 1) // 2
        for j in range(s,e+1):
            cnt[j] +=1
    print(f'#{tc} {max(cnt)}')