def solution(sticker):
    answer = 0
    n = len(sticker)
    if n==1:
        return sticker[0]
    # 첫번째를 뗀경우
    data1 = [0]*n
    
    data1[0]=sticker[0]
    data1[1] = data1[0]
    for i in range(2,n-1):
        data1[i] = max(data1[i-2]+sticker[i],data1[i-1])
    data2 = [0]*n
    data2[1] = sticker[1]
    for i in range(2,n):
        data2[i] = max(data2[i-2]+sticker[i],data2[i-1])
    # print(data1,data2)
    return max(max(data1),max(data2))
