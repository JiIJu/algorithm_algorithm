from collections import deque
def solution(rows, columns, queries):
    answer = []
    data = [[0]*columns for _ in range(rows)]
    n=1
    for i in range(rows):
        for j in range(columns):
            data[i][j]=n
            n+=1
    for x1,y1,x2,y2 in queries:
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        temp = data[x1][y1]
        minv = temp
        for i in range(x1,x2):
            data[i][y1] = data[i+1][y1]
            minv = min(minv,data[i][y1])
        for i in range(y1,y2):
            data[x2][i]=data[x2][i+1]
            minv = min(minv,data[x2][i])
        for i in range(x2,x1,-1):
            data[i][y2] = data[i-1][y2]
            # print(data[i][y2])
            minv = min(minv,data[i][y2])
        for i in range(y2,y1,-1):
            data[x1][i] = data[x1][i-1]
            # print(data[x1][i])
            minv = min(minv,data[x1][i])
        data[x1][y1+1]=temp
        answer.append(minv)
    return answer
