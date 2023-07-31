# swea 1240 단순 2진암호코

password = {
    '0001101' : '0',
    '0011001' : '1',
    '0010011' : '2',
    '0111101' : '3',
    '0100011' : '4',
    '0110001' : '5',
    '0101111' : '6',
    '0111011' : '7',
    '0110111' : '8',
    '0001011' : '9'
}

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M-56):
            temp = 1
            # print((data[i:i+7]))
            if ''.join(data[i][j:j+7]) in password:
                for k in range(0,56,7):
                    # print(''.join(data[i][j + k:j + k + 7]))
                    if ''.join(data[i][j+k:j+k+7]) not in password:
                        # print(''.join(data[i][j + k:j + k + 7]))
                        temp = 0
                        break
                    elif ''.join(data[i][j+k:j+k+7]) in password:
                        temp=2
            ans = ''
            if temp==2:
                for k in range(0, 56, 7):
                    ans+= password[''.join(data[i][j+k:j+k+7])]
                break
        if temp==2:
            break
    check = (int(ans[0]) + int(ans[2]) + int(ans[4]) + int(ans[6]))*3 + (int(ans[1])+int(ans[3])+int(ans[5])+int(ans[7]))
    answer = 0
    for i in ans:
        answer+=int(i)
    if not check%10:
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} 0')


