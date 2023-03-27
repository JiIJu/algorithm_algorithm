from itertools import permutations
def check(user,ban):
    if len(user)!=len(ban):
        return False
    for i in range(len(ban)):
        if ban[i]=='*':
            continue
        elif user[i] != ban[i]:
            return False
    return True
        
def solution(user_id, banned_id):
    answer = []
    n,k = len(user_id) , len(banned_id)
    data = list(permutations(user_id,k))
    for i in data:
        temp = True
        for j in range(k):
            if not check(i[j],banned_id[j]):
                temp = False
        if temp:
            if set(i) not in answer:
                answer.append(set(i))
    return len(answer)