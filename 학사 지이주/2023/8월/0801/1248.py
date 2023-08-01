# swea 1248 공통조상
def dfs1(start,check):
    for d in data[start]:
        if d == a:
            for i in check:
                node1.append(i)
            return
        dfs1(d,check+[d])
def dfs2(start,check):
    for d in data[start]:
        if d == b:
            for i in check:
                node2.append(i)
            return
        dfs2(d,check+[d])
def dfs3(start):
    global maxv
    for d in data[start]:
        maxv+=1
        dfs3(d)
T = int(input())
for tc in range(1,T+1):
    V , E , a , b = map(int,input().split())
    node = list(map(int,input().split()))
    data = [[] for _ in range(V+1)]
    for i in range(0,E*2,2):
        data[node[i]].append(node[i+1])
    node1 , node2 = [1],[1]
    dfs1(1,[])
    dfs2(1,[])
    same = []
    if a>=b:
        for i in node1:
            if i in node2:
                same.append(i)
    else:
        for i in node2:
            if i in node1:
                same.append(i)
    maxv = 1
    dfs3(same[-1])
    print(f'#{tc} {same[-1]} {maxv}')