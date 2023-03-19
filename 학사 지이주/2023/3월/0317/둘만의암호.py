def solution(s, skip, index):
    answer = ''
    # ord , chr
    print(ord('a'),ord('z'))
    s = list(s)
    skip = list(skip)
    for i in s:
        temp = ord(i)
        cnt = 0
        while cnt < index:
            temp +=1
            if temp>ord('z'):
                temp = ord('a')
            if chr(temp) not in skip:
                cnt+=1
        answer += chr(temp)
    return answer
