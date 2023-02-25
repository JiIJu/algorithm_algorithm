# HMAT 스마트물류

import sys

N,K = map(int,input().split())
data = list(input())

ans = 0
for i in range(N):
    temp=0
    if data[i]=='P':
        for j in range(K,0,-1):
            if 0<=i-j<N and data[i-j]=='H':
                data[i-j] = 'p'
                ans+=1
                temp = 1
                break
        if temp==0:
            for j in range(1,K+1):
                if 0<=i+j<N and data[i+j]=='H':
                    data[i+j]='p'
                    ans+=1         
                    break

print(ans)
