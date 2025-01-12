def solution(n, words):
    answer = []
    word_list = [words[0]]
    temp = dict([])
    temp[words[0]]=1
    for i in range(1,len(words)):
        if words[i] not in temp and word_list[-1][-1] == words[i][0]:
            word_list.append(words[i])
            temp[words[i]] = 1
        else:
            return [(i)%n+1,(i)//n+1]
        # print(temp)

    return [0,0]