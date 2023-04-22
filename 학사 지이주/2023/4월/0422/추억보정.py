def solution(name, yearning, photo):
    answer = []
    n = len(name)
    data = {}
    for i in range(n):
        data[name[i]] = yearning[i]
    for i in photo:
        temp = 0
        # print(i)
        for j in i:
            if j in data:
                temp += data[j]
        answer.append(temp)
    return answer