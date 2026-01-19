T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    dist = [[0]*N for _ in range(N)]
    dist[0][0] = board[0][0]

    for i in range(1, N):
        dist[i][0] = board[i][0] + dist[i-1][0]
        dist[0][i] = board[0][i] + dist[0][i-1]

    for i in range(1, N):
        for j in range(1, N):
            dist[i][j] = min(dist[i-1][j], dist[i][j-1]) + board[i][j] 

    result = dist[N-1][N-1]
    print(f"#{test_case} {result}")