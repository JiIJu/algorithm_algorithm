def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if len(answer)>=1:
            if answer[-1] != i:
                answer.append(i)
        else:
            answer.append(i)
    return answer
