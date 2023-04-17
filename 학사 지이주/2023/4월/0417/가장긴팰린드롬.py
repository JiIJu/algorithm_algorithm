def solution(s):
    answer = []
    n = len(s)
    a=n
    while True:
        print(a)
        for i in range(n-a+1):
            temp = s[i:a+i]
            # print(i,a)
            if temp == temp[::-1]:
                # print(temp)
                return len(temp)
        a-=1
        