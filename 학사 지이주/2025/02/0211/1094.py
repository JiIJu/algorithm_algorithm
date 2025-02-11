# https://www.acmicpc.net/problem/1094


n = int(input())
a = ''
while n>0:
    a += str(n%2)
    n=n//2
a = a[::-1]
print(a.count('1'))