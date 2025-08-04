def solution(routes):
    answer = 1
    routes = sorted(routes,key = lambda x : (x[1],x[0]))
    
    check = routes[0][1]

    for i in range(1,len(routes)):
        if check >= routes[i][0]:

            pass
        else:

            check = routes[i][1]
            answer+=1
        
    return answer
