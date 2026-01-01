import sys

N=int(sys.stdin.readline().strip())

dp = [0]*(1000001)
dp[1]=0

for i in range(2, N+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)    # d[i]: 1을 빼는 연산, dp[i//2]: 2로 나누는 연산 -> 1을 뺀 놈과 2로 나눈 놈 중 최솟값 +1
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
    """
    if i%3==0:
        dp[i]=min(dp[i//3]+1, dp[i-1]+1)
    elif i%2==0: -> '3으로 나누어 떨어지지 않으면 2로 나누어본다'가 아니라 다 나눠보고 최솟값을 찾아야 함. elif 쓰면 안됨
        dp[i]=min(dp[i//2]+1, dp[i-1]+1)
    else:
        dp[i]=dp[i-1]+1
    """
print(dp[N])

"""
1 1
2 1
3 1
4 2
5 3
6 2
7 3
8 3
9 2
10 3
"""