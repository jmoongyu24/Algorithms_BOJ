T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    times = [list(map(int,input().split())) for _ in range(N)]
    times.sort(key = lambda x: [x[1], x[0]])

    result = 0
    end_time = 0

    for s,e in times:
        if s >= end_time:
            result += 1
            end_time = e
    
    print(f"#{test_case} {result}")