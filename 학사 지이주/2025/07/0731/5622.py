# 5622 


data = list(input())

ans =0

dire = {'ABC' : 2, 'DEF' : 3, 'GHI' : 4 , 'JKL' : 5, 'MNO' : 6, 'PQRS' : 7, 'TUV' : 8, 'WXYZ' : 9}

for i in data:
    for j in dire:
        temp =0
        for k in j:
            # print(i,k)
            if i == k:
                # print(j,dire[j])
                ans += 1+dire[j]
                temp=1
                break
        if temp:
            break
print(ans)

            
        

