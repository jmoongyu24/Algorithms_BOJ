import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0

    for num in nums:
        result += num
    result = round(result/len(nums))
    print(f"#{test_case} {result}")