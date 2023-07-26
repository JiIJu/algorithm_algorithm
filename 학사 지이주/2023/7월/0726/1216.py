# swea 1216 회문2

for tc in range(1,11):
    N = int(input())
    data = [list(input()) for _ in range(100)]
    maxv = 0
    for i in range(100):
        temp = 0
        check = 0
        for j in range(99,-1,-1):
            if j < maxv:
                break
            for k in range(temp+1):
                a = data[i][k:j+k+1]
                if a == a[::-1]:
                    maxv = max(maxv,len(a))
                    check=1
                    break
            if check:
                break
            else:
                temp+=1
    test = []
    for i in range(100):
        a = []
        for j in range(100):
            a.append(data[j][i])
        print(a)
        test.append(a)
    for i in range(100):
        temp = 0
        check = 0
        for j in range(99,-1,-1):
            if j <= maxv:
                break
            for k in range(temp+1):
                a = test[i][k:j+k+1]
                if a == a[::-1]:
                    maxv = max(maxv,len(a))
                    check=1
                    break

            if check:
                break
            else:
                temp+=1
    for i in range(100):
        temp = 0
        check = 0
        for j in range(99,-1,-1):
            if j < maxv:
                break
            for k in range(temp+1):
                a = data[i][k:j+k]
                if a == a[::-1]:
                    maxv = max(maxv,len(a))
                    check=1
                    break
            if check:
                break
            else:
                temp+=1
    test = []
    for i in range(100):
        a = []
        for j in range(100):
            a.append(data[j][i])
        print(a)
        test.append(a)
    for i in range(100):
        temp = 0
        check = 0
        for j in range(99,-1,-1):
            if j <= maxv:
                break
            for k in range(temp+1):
                a = test[i][k:j+k]
                if a == a[::-1]:
                    maxv = max(maxv,len(a))
                    check=1
                    break

            if check:
                break
            else:
                temp+=1

    print(f'#{tc} {maxv}')
