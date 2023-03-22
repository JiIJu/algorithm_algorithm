def solution(n, costs):
    ans = 0
    costs.sort(key=lambda x:x[2])
    data = set([costs[0][0]])
    
    while len(data)!=n:
        for cost in costs:
            if cost[0] in data and cost[1] in data:
                continue
            if cost[0] in data or cost[1] in data:
                data.update([cost[0],cost[1]])
                ans+=cost[2]
                break

    return ans
