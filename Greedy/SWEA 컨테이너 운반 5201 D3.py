T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    load = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    load.sort(reverse = True)
    truck.sort(reverse = True)

    result = 0

    for t in truck:
        for i in range(len(load)):
            if load[i] <= t and load[i] != 0:
                result += load[i]
                load[i] = 0
                break

    print(f"#{test_case} {result}")            