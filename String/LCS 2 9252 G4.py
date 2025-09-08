import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n = len(str1)
m = len(str2)

# LCS 1 문제와는 다르게 dp에 문자열 길이가 아닌 문자열 자체를 저장
dp = [[''] * (m+1) for _ in range(n+1)]

# 논리는 비슷함
for i in range(1, n+1):
    for j in range(1, m+1):
        # 만약 직전 두 문자가 같다면 같은 문자열을 dp[i][j]에 추가 
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+str1[i-1]
        else:
            # 직전 두 문자가 다르다면, dp[i-1][j]와 dp[i][j-1] 중 더 긴 문자열을 dp[i][j]에 추가
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[n][m]))
print(dp[n][m] if dp[n][m] else exit(0))