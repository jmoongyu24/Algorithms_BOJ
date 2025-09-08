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

"""
# 이렇게도 풀 수 있음 
# 내 풀이는 직전 문자가 같을 경우 직전 문자를 현재 dp에 추가하는 방식이었는데
# 이 풀이는 현재 문자가 같을 경우 현재 문자를 dp에 추가하는 방식임

# [0]을 추가해서 [0][0]에 빈공간 만들어둠. 그래야 현재 문자를 기준으로 비교 가능
# 내 기존 풀이는 [0]이 없어서 이전 문자를 기준으로 비교했었음
str1 = [0] + list(input())
str2 = [0] + list(input())

len_1 = len(str1)
len_2 = len(str2)

array = [['' for _ in range(len_1)] for _ in range(len_2)]

for i in range(1, len_2) :
    for j in range(1, len_1) :
        # 만약 현재 문자가 같으면 직전에 알고 있던 dp에 현재 문자 추가
        if str1[j] == str2[i] :
            array[i][j] = array[i-1][j-1] + str1[j]
        # 만약 현재 문자가 다르면 직전까지 알고 있던 dp 중 더 긴 문자열을 현재 dp에 추가
        else :
            if len(array[i][j-1]) > len(array[i-1][j]) :
                array[i][j] = array[i][j-1]
            else : 
                array[i][j] = array[i-1][j]

answer = len(array[-1][-1])
print(answer)
if answer != 0 :
    print(array[-1][-1])
출처: https://think-tech.tistory.com/55 [자윰이의 성장일기:티스토리]
"""