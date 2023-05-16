def solution(picks, minerals):
    answer = 0
    n = len(minerals)
    if sum(picks)*5 < n:
        minerals = minerals[:sum(picks)*5]
    data = []
    n = len(minerals)
    for i in range(0,n,5):
        temp = []
        if i+5<n:
            for j in range(5):
                temp.append(minerals[i+j])
        else:
            for j in range(n-i):
                temp.append(minerals[i+j])
        data.append(temp)
    score = []
    for i in range(len(data)):
        score.append([0,0,0])
    for i in range(len(data)):
        for j in data[i]:
            if j=='diamond':
                score[i][0]+=1
                score[i][1]+=5
                score[i][2]+=25
            elif j=='iron':
                score[i][0]+=1
                score[i][1]+=1
                score[i][2]+=5
            elif j=='stone':
                score[i][0]+=1
                score[i][1]+=1
                score[i][2]+=1
    score.sort(key=lambda x:(x[2],x[1],x[0]))
    
    for i in range(len(picks)):
        for j in range(picks[i]):
            if score:
                answer += score.pop()[i]
            else:
                return answer
    return answer
