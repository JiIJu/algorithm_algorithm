import sys

n, k =  map(int,input().split())

a = list(map(int, input().split()))

for _ in range(k):
    b, c = map(int, input().split())
    ans = sum(a[b-1:c])
    ans = ans/(c-b+1)
    print(f"{ans:.2f}")

######
# 오늘 새롭게 알게된것 f"{ans:.2f}"
######
