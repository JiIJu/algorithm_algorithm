# swea 1213 String

for tc in range(1,11):
    T = int(input())
    word = input()
    data = input()
    ans = 0
    for i in range(len(data)-len(word)+1):
        if data[i:i+len(word)] == word:
            ans+=1
    print(f'#{tc} {ans}')