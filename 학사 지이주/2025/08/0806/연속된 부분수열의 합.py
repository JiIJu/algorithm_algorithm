from collections import deque
def solution(sequence, k):
    answer = []
    data = deque([])
    sumv = 0
    temp = deque([])
    for i in range(len(sequence)):
        # print(111,sumv , temp,i)
        while temp and sumv+sequence[i] > k:
            sumv -= sequence[temp.popleft()]
        if sumv+sequence[i]<=k:
            sumv += sequence[i]
            temp.append(i)

        if sumv == k:
            # print('why???')
            data.append([temp[0],temp[-1]])

        # print(f'sumv : {sumv}')
        # print(f'temp : {temp}')
        # print(f'data : {data}')
    minv = 99999999
    check = []
    for i,j in data:

        if minv > j-i:
            minv = j-i
            check = [i,j]

    return check


    
