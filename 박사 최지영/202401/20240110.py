def solution(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))

def solution(s):
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer
