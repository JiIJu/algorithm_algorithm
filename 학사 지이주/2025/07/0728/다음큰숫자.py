def solution(n):
    answer = 0
    temp, cnt = second(n)

    next = n + 1
    check = False
    while not check:
        temp2, next2 = second(next)
        if next2 == cnt:
            check = True

            return next
        next += 1


def second(n):
    a = ''
    cnt = 0
    while n:
        a += str(n % 2)
        if n % 2 == 1:
            cnt += 1
        n = n // 2

    return a[::-1], cnt