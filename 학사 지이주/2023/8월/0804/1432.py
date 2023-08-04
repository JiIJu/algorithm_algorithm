# swea 1234 비밀번호
from collections import deque
for tc in range(1,11):
    N , data = input().split()
    data = deque(list(data))
    ans = deque([])
    while data:
        if ans and data[0]==ans[-1]:
            data.popleft()
            ans.pop()
        else:
            ans.append(data.popleft())
        # print(ans)
    print(f'#{tc} {"".join(ans)}')
