from collections import deque
def solution(topping):
    answer = 0
    a,b = dict([]),dict([])
    for i in topping:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    
    for i in topping:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
        if i in a:
            if a[i]>1:
                a[i]-=1
            else:
                del a[i]
        if len(a)==len(b):
            answer+=1
            # print(a,b)
            
    return answer