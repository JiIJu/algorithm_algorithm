def solution(s):
    answer = ''
    s = list(s.split())
    listv = [0]*len(s)
    # print(s)
    for i in range(len(s)):
        # print(s)
        listv[i] = int(s[i])
        
    # print(listv)
    listv = sorted(listv)
    answer = str(listv[0]) + ' ' + str(listv[-1])
    return answer