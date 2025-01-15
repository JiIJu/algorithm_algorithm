def solution(arr1, arr2):
    answer = []
    arr1_len1 = len(arr1)
    arr1_len2 = len(arr1[0])
    arr2_len1 = len(arr2)
    arr2_len2 = len(arr2[0])

    for i in range(arr1_len1):
        ans = []
        for j in range(arr2_len2):
            temp = 0
            for k in range(arr2_len1):
                temp += arr1[i][k] * arr2[k][j]
            ans.append(temp)
        answer.append(ans)
    return answer