def solution(genres, plays):
    answer = []
    total = {}
    data = {}
    for i in range(len(genres)):
        if genres[i] in total.keys():
            total[genres[i]] += plays[i]
            data[genres[i]].append((i,plays[i]))
        else:
            data[genres[i]] = [(i,plays[i])]
            total[genres[i]] = plays[i]
    total = sorted(total.items(),key=lambda x:x[1] , reverse= True)
    
    for i in total:
        temp = sorted(data[i[0]],key=lambda x:x[1],reverse=True)
        for j in range(len(temp)):
            if j==2:
                break
            answer.append(temp[j][0])
        
            
    return answer
