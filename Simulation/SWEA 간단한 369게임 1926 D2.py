import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    result = ""
    for i in range(1,N+1):
        s_i = str(i)
        if '3' in s_i or '6' in s_i or '9' in s_i:
            result += "-" * s_i.count('3') + "-" * s_i.count('6') + "-" * s_i.count('9') + " "
        else:
            result += s_i + " "
    print(result.strip())