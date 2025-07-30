def solution(want, number, discount):
    answer = 0
    data = {}
    n = sum(number)
    for i in range(len(want)):
        data[want[i]] = number[i]
    if len(discount)>=10:
        for i in range(len(discount)-9):
            temp = 1
            temp_data = discount[i:i+10]
            for j in data:
                if data[j] > temp_data.count(j): 
                    temp = 0
                    break
            if temp:
                print(i)
                answer +=1
    else:
        temp=1
        for j in data:
            
            if data[j] > discount.count(j): 
                temp = 0
                break
        if temp:
            print(i)
            answer +=1
    return answer