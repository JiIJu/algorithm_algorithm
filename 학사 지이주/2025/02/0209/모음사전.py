from itertools import product
def solution(word):
    answer = 0
    
    temp = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    print(list(product(vowels,repeat=2)))
    # combinations = list(product(vowels, repeat=2)) 
    # print(combinations)
    for i in range(1,6):
        for j in list(product(vowels, repeat=i)):
            temp.append(''.join(j))
    temp.sort()
    

    return temp.index(word)+1