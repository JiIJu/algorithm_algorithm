# 4375 1
while True:
    try:
        N = int(input())
    except:
        break
    ans = 1
    temp = 0
    while True:
        temp = temp*10 + 1
        temp = temp%N
        if temp == 0:
            print(ans)
            break
        ans +=1
