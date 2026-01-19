T = int(input())

for test_case in range(1, T + 1):
    N = float(input())
    result = ""
    count = 0

    while N > 0 and count < 12:
        N *= 2
        if N >= 1:
            result += "1"
            N -= 1
        else:
            result += "0"
        count += 1

    if N > 0:  # 12자리 이상 필요할 경우
        print(f"#{test_case} overflow")
    else:
        print(f"#{test_case} {result}")