
def solution(numbers):
    answer = [0]*len(numbers)
    n = len(numbers)
    answer[n-1] = -1
    for i in range(n-2,-1,-1):
        if numbers[i+1]>numbers[i]:
            answer[i] = numbers[i+1]
        else:
            j = i+1
            while j<n and answer[j]!=-1:
                if answer[j]>numbers[i]:
                    answer[i] = answer[j]
                    break
                j+=1
            if j==n or answer[j]==-1:
                answer[i]=-1
        # elif answer[i+1]>numbers[i]:
        #     answer[i] = answer[i+1]
        # else:
        #     answer[i] = -1
    return answer
