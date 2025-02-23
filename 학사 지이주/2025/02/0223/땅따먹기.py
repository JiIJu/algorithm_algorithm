def solution(land):
    answer = 0
    temp = [land[0]]
    for i in range(1,len(land)):
        temp.append([0,0,0,0])
    for i in range(1,len(land)):
        for j in range(4):
            for k in range(4):
                if j!=k:
                    temp[i][j] = max(temp[i][j],temp[i-1][k]+land[i][j])
                    # print(temp,i,j,k)
                    # print(temp[i][j],temp[i][j],temp[i-1][j]+land[i][k])
    return max(temp[-1])