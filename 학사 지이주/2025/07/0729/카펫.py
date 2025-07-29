def solution(brown, yellow):
    answer = []
    total = brown + yellow 
    for i in range(3,total):
        j = total//i
        if not total % i:
            if (i-2)*(j-2) == yellow:
                return [j,i]
            
    
    return answer