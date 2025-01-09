def gcd(a,b):
    temp = 1
    while b:
        temp = a
        a = b
        b = temp%b
    return a
        
        
def solution(arr):
    answer = 1
    
    answer = arr[1]*arr[0]
    a = gcd(arr[1],arr[0])
    answer = answer//a
    for i in range(1,len(arr)):
        if i >1:
            if arr[i]>a:
                a = gcd(answer,arr[i])
            else:
                a = gcd(arr[i],answer)
            answer *=arr[i] //a
        # print(answer,a , arr[i])
    return answer