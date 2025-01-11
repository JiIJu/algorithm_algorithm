def solution(elements):
    answer = 0
    extended_elements = elements*2
    temp = dict([])
    # print(extended_elements)
    for i in range(len(elements)):
        temp2= 0
        for j in range(len(elements)):
            temp2+=extended_elements[i+j]
            if temp2 not in temp:
                temp[temp2]=1
    # print(sorted(list(temp.keys())))
    return len(temp)