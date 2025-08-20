# 25206 너의 평점은


data = []
score = {'A+':4.5 , 'A0' : 4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for i in range(20):
    data.append(list(input().split()))
ans = 0.0
check = 0
for i,j,k in data:
    if k=='P':
        pass
    else:
        ans += score[k]*float(j)
        check += float(j)
print(ans/check)