import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n = len(str1)
m = len(str2)

# DP 테이블 / 문자열 2개를 한 문자씩 비교하므로 2차원 리스트로 표현하는 것이 적절함
dp = [[0] * (m+1) for _ in range(n+1)]

# 입력받은 두 문자열의 길이대로 생성한 DP 테이블을 채워나감
for i in range(1, n+1):
    for j in range(1, m+1):
        # 만약 현재 두 문자열의 문자가 같다면, 직전까지의 lcs 길이(dp[i-1][j-1]) + 1
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        # 만약 현재 두 문자열의 문자가 다르다면, 직전까지의 lcs 길이 중 더 큰 값
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])