str1 = list(input())
str2 = list(input())

lcs = [[0] * 1001 for _ in range(1001)] # 두 문자열을 비교할 LCS DP 2차원 리스트

for i in range(1, len(str1)+1): # str1 앞부터 순차 탐색
    for j in range(1, len(str2)+1): # str2 앞부터 순차 탐색
        # 현재 위치끼리 비교했을 때, 같으면 직전 lcs + 1
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
            
        # 현재 위치끼리 비교했을 때, 다르면 lcs + 0 (= 기존 lcs 값 중 최댓값 유지)
        # 1. i 위치의 str1(현재)과 j-1 위치의 str2(직전)의 LCS
        # 2. i-1 위치의 str1(직전)과 j 위치의 str2(현재)의 LCS
        # 1과 2 중 최댓값을 현재 위치 i & j의 LCS 값으로 선정
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(max(map(max, lcs)))