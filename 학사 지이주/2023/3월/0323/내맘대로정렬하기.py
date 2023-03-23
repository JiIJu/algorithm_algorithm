def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(list(i))
    answer.sort(key=lambda x:(x[n],x))
    ans = []
    for i in answer:
        temp = ''
        for j in i:
            temp +=j
        ans.append(temp)
    return ans
