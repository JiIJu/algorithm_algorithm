# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    
    phone_book.sort(key=lambda  x:(x,len(x)))
    # print(phone_book)
    for i in range(len(phone_book)-1):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
    return answer