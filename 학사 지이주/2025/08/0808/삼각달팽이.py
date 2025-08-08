def solution(n):
    answer = []
    data = [[0] * i for i in range(1,n+1)]
    num = 1
    x=-1
    y=0
    
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x +=1
            elif i%3 == 1:
                y +=1
            elif i%3 == 2:
                x-=1
                y-=1
            data[x][y] = num
            num +=1
    ans = []
    for i in data:
        for j in i:
            ans.append(j)
    return ans