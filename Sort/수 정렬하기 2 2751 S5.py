import sys
N = int(input())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)