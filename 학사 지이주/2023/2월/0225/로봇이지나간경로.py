
import sys

H,W = map(int,input().split())
data = [list(sys.stdin.readline()) for _ in range(H)]

di = [-1,0,1,0]
dj = [0,1,0,-1]
order = 'A'
direction = ''
temp = 0
stack = []
def path(i,j,direct):
    if 0<=i+di[direct]<H and 0<=j+dj[direct]<W and data[i+di[direct]][j+dj[direct]]=='#':
        return True
    else:
        return False

for i in range(H):
    for j in range(W):
        if data[i][j]=='#':
            a = path(i,j,0)
            b = path(i,j,1)
            c = path(i,j,2)
            d = path(i,j,3)
            if a+b+c+d == 1:
                start = [i,j]
                temp = 1
                stack.append([i,j])
                data[i][j] = '.'
                if a:
                    direction += '^'
                elif b:
                    direction += '>'
                elif c:
                    direction += 'v'
                elif d :
                    direction += '<'
                break
    if temp:
        break

# ^ v < >
while stack:
    a,b = stack.pop()
    if direction[-1] == '^':
        for i in range(2):
            a-=1
            data[a][b] = '.'
    elif direction[-1] == 'v':
        for i in range(2):
            a+=1
            data[a][b] = '.'
    elif direction[-1] == '<':
        for i in range(2):
            b-=1
            data[a][b] = '.'
    elif direction[-1] == '>':
        for i in range(2):
            b+=1
            data[a][b] = '.'
    stack.append([a,b])
    if path(a,b,0):
        direction +='^'   
    elif path(a,b,1):
        direction +='>'
    elif path(a,b,2):
        direction +='v'
    elif path(a,b,3):
        direction +='<'
    else:
        stack.pop()

tmp_direction = direction[0]

for i in range(1,len(direction)):
    if tmp_direction == direction[i]:
        order += 'A'
    else:
        if tmp_direction == '>':
            if direction[i] == '^':
                order += 'LA'
            elif direction[i] == 'v':
                order += 'RA'
        elif tmp_direction == '<':
            if direction[i] == '^':
                order += 'RA'
            elif direction[i] == 'v':
                order += 'LA'
        elif tmp_direction == '^':
            if direction[i] == '>':
                order += 'RA'
            elif direction[i] == '<':
                order += 'LA'
        elif tmp_direction == 'v':
            if direction[i] == '>':
                order += 'LA'
            elif direction[i] == '<':
                order += 'RA'
    tmp_direction = direction[i]

print(start[0]+1,start[1]+1)
print(direction[0])
print(order)
