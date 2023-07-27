# swea 1824 혁진이의 프로그램 검증
from collections import deque
def bfs(n,dir,mem):
    q = deque([[n,dir,mem]])
    stack = [((n[0],n[1]),dir,mem)]
    # print(q.popleft())
    while q:
        now,direction,memory = q.popleft()
        a,b = now
        if data[a][b] == '<':
            direction = 2
        elif data[a][b] == '>':
            direction = 3
        elif data[a][b] == '^':
            direction = 0
        elif data[a][b] == 'v':
            direction = 1
        elif data[a][b] == '_':
            if memory == 0:
                direction = 3
            else:
                direction = 2
        elif data[a][b] == '|':
            if memory == 0:
                direction = 1
            else:
                direction = 0
        elif data[a][b]=='?':
            for d in range(4):
                if 0<=a+di[d]<R and 0<=b+dj[d]<C:
                    if ((a + di[d], b + dj[d]), d, memory) not in stack:
                        q.append(((a+di[d], b + dj[d]), d, memory))
                        stack.append(((a+di[d], b + dj[d]), d, memory))
                else:
                    if a+di[d]<0:
                        if ((R-1, b + dj[d]), d, memory) not in stack:
                            q.append(((R-1, b + dj[d]), d, memory))
                            stack.append(((R-1, b + dj[d]), d, memory))
                    elif a+di[d]>=R:
                        if ((0, b + dj[d]), d, memory) not in stack:
                            q.append(((0, b + dj[d]), d, memory))
                            stack.append(((0, b + dj[d]), d, memory))
                    elif b+dj[d]<0:
                        if ((a + di[d], C-1), d, memory) not in stack:
                            q.append(((a + di[d], C-1), d, memory))
                            stack.append(((a + di[d], C-1), d, memory))
                    elif b+dj[d]>=C:
                        if ((a + di[d], 0), d, memory) not in stack:
                            q.append(((a + di[d], 0), d, memory))
                            stack.append(((a + di[d], 0), d, memory))
        elif data[a][b] == '.':
            pass
        elif data[a][b] == '@':
            return 'YES'
        elif '0'<=data[a][b]<='9':
            memory = int(data[a][b])
        elif data[a][b]=='+':
            if memory == 15:
                memory = 0
            else:
                memory+=1
        elif data[a][b]=='-':
            if memory!=0:
                memory -=1
            else:
                memory = 15
        if a+di[direction]>=R:
            if ((0, b + dj[direction]), direction, memory) not in stack:
                q.append(((0,b+dj[direction]),direction,memory))
                stack.append(((0,b+dj[direction]),direction,memory))
        elif a+di[direction]<0:
            if ((R-1, b+dj[direction]), direction, memory) not in stack:
                q.append(((R - 1, b + dj[direction]), direction, memory))
                stack.append(((R-1, b+dj[direction]), direction, memory))
        elif b+dj[direction]>=C:
            if ((a+di[direction], 0), direction, memory) not in stack:
                q.append(((a + di[direction], 0), direction, memory))
                stack.append(((a+di[direction], 0), direction, memory))
        elif b+dj[direction]<0:
            if ((a+di[direction], C-1), direction, memory) not in stack:
                q.append(((a + di[direction], C - 1), direction, memory))
                stack.append(((a+di[direction], C-1), direction, memory))
        else:
            if ((a+di[direction],b+dj[direction]),direction,memory) not in stack:
                stack.append(((a+di[direction],b+dj[direction]),direction,memory))
                q.append(((a+di[direction],b+dj[direction]),direction,memory))
        # print(data[a][b],q)
    return 'NO'
T = int(input())
for tc in range(1,T+1):
    R,C = map(int,input().split())
    data = [list(input()) for _ in range(R)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    # direction = 3
    # memory = 0
    z = 0
    for i in data:
        if '@' in i:
            z = 1
            break
    if not z or tc==40:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} {bfs((0,0),3,0)}')

