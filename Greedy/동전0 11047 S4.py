import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
result = 0

for _ in range(N):
    coin.append(int(input()))

# 역순 순차 탐색을 위한 동전 정렬
coin.sort(reverse = True)

for c in coin:
    # 더 이상 만들 수 있는 금액이 없으면 break
    if K == 0:
        break
    # 현재 금액에서 사용할수 있는 최대 동전 개수  K//c
    # 만들고 남은 금액 K %= c
    result += K // c
    K %= c

print(result)