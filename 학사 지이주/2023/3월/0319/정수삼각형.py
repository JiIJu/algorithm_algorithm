def solution(triangle):
    answer = 0
    data = [[0]*i for i in range(1,len(triangle)+1)]
    data[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        data[i][0] = data[i-1][0]+triangle[i][0]
        data[i][-1] = data[i-1][-1]+triangle[i][-1]
    for i in range(1,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            # print(i,j)
            data[i][j] = max(data[i][j],data[i-1][j-1]+triangle[i][j],data[i-1][j]+triangle[i][j])
    return max(data[-1])
