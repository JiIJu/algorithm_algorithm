def dfs(a,data,visit):
    visit[a]=1
    for i in data[a]:
        if not visit[i]:
            
            dfs(i,data,visit)
            
def solution(n, results):
    answer = 0
    data = [[] for _ in range(n)]
    for i,j in results:
        data[i-1].append(j-1)
    visit = [0]*n
    temp = []
    for i in range(n):
        dfs(i,data,visit)
        temp.append(visit)
        visit = [0]*n
    temp_data = []
    for i in range(len(temp)):
        new_visit = [0]*n
        for j in range(len(temp)):
            if temp[i][j] or temp[j][i]:
                new_visit[j] = 1
        temp_data.append(new_visit)
    for i in temp_data:
        if sum(i)==n:
            answer+=1
    return answer
