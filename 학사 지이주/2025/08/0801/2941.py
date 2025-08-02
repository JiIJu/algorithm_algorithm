from collections import deque
data = list(input())

temp = deque([])
ans = 0
alpha = {'c=':1,'c-':1,'dz=':1,'d-':1,'lj':1,'nj':1,'s=':1,'z=':1}

n = len(data)
i=0
while i<n:
    temp = ''
    check = 0

    if i+2<n:
        temp = data[i] + data[i+1] + data[i+2]
        
        if temp in alpha:
            ans+=1
            i +=3
            check = 1
    if not check and i+1<n:
        temp = data[i] + data[i+1]
        if temp in alpha:
            
            ans+=1
            i +=2
            check = 1
    if not check:
        i+=1
        ans+=1
        

print(ans)