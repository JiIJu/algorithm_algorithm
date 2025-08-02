

a,b,v = map(int,input().split())

v1 = v - a
c=a-b

if v1%c>0:
    cnt = v1//c+1
else:
    cnt = v1//c

print(cnt+1)