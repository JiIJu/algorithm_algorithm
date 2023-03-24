def solution(s, n):
    answer = ''
    # ord , chr
    for i in s:
        if 'a'<=i<='z':
            if ord(i)+n>ord('z'):
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        elif 'A'<=i<='Z':
            if ord(i)+n>ord('Z'):
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        else:
            answer +=i
    return answer
