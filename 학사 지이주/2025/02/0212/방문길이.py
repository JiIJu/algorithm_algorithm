def solution(dirs):
    answer = 0
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    i,j=0,0
    data = set()
    dirs = list(dirs)
    a=0
    for q in dirs:
        if q =='U':
            a = 0
        elif q == 'D':
            a = 1
        elif q == 'R':
            a = 2
        elif q == 'L':
            a = 3

        if -5<=i+di[a]<=5 and -5<=j+dj[a]<=5:
            ni = i + di[a]
            nj = j + dj[a]
            data.add((i,j,ni,nj))
            data.add((ni,nj,i,j))
            # print(i,j,ni,nj)
        i = ni
        j = nj
    # print(data)
    return len(data)//2