N = int(input())
data = [0]*301

for i in range(N):
    data[i]=(int(input()))
s= [0]*(301)
n=0

s[0] = data[0]
s[1] = data[0]+data[1]
s[2] = max(data[0]+data[2],data[1]+data[2])
for i in range(3,N):
    s[i] = max(s[i-3]+data[i-1]+data[i],s[i-2]+data[i])
print(s[N-1])