def solution(brown, yellow):
    answer = []
    total = brown + yellow
    temp = []
    for i in range(1,total+1):
        if total%i == 0:
            temp.append(i)
    temp2 = []
    for i in temp:
        temp2.append(total//i)
    for i in range(len(temp)):
        if (temp[i]-2)*(temp2[i]-2)==yellow:
                return [temp2[i],temp[i]]
    