n = int(input())
candidate = []
for i in range(n):
    a = int(input())
    candidate.append(a)
ans=0
dasom = candidate[0]
if len(candidate)==1:
    pass
else:
    while dasom <= max(candidate):
        i = candidate.index(max(candidate))
        dasom+=1
        candidate[i]-=1
        ans +=1

print(ans)