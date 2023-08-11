import string
import math
def solution(str1, str2):
    answer = 0
    str1,str2 = str1.upper() , str2.upper()
    check1,check2,check3,check4 = {},{},{},{}
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            temp1  = str1[i] + str1[i+1]
            if temp1 not in check1:
                check1[temp1]=1
            else:
                check1[temp1]+=1
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            temp2  = str2[i] + str2[i+1]      
            if temp2 not in check2:
                check2[temp2]=1
            else:
                check2[temp2] += 1
    for i in check1:
        if i in check2:
            check3[i] = min(check1[i],check2[i])
        check4[i] = check1[i]
    for i in check2:
        if i in check4:
            check4[i] = max(check2[i],check1[i])
        else:
            check4[i] = check2[i]
    ans1,ans2 = 0,0
    for i in check3:
        ans1+=check3[i]
    for i in check4:
        ans2+=check4[i]
    if not ans1 and not ans2:
        return 65536
    answer = math.floor((ans1/ans2)*65536)
    
    return answer
