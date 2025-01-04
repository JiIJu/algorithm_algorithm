def solution(s):
    answer = [0 ,0]
    while s != '1':
        temp_s=''
        for i in s:
            if i == '1':
                temp_s +='1'
            else:
                answer[1]+=1
        temp_second = ''
        len_temps = len(temp_s)
        while len_temps:
            temp_second = str(len_temps%2) + temp_second
            len_temps = len_temps//2
        s = temp_second
        answer[0]+=1
    
    return answer