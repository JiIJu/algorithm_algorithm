def gcd(a,b):
    if a<b:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a
def solution(arrayA, arrayB):
    answer = 0
    gcdA,gcdB = 0,0
    for i in range(len(arrayA)):
        gcdA = gcd(gcdA,arrayA[i])
        gcdB = gcd(gcdB,arrayB[i])
    print(gcdA,gcdB)
    for i in range(len(arrayA)):
        if arrayA[i]%gcdB == 0:
            gcdB=1
        if arrayB[i]%gcdA==0:
            gcdA=1
    if gcdA==1 and gcdB==1:
        return 0
    else:
        return max(gcdA,gcdB)
