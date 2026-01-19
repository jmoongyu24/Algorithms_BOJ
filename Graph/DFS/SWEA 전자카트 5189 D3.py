def dfs(cnt, now, total): # cnt: 현재까지 방문한 구역 수, now: 현재 구역, total: 현재까지 배터리 소비량
    global answer

    if cnt == N:  # 모든 구역을 방문한 경우
        total += board[now][0]  # 사무실로 돌아오는 비용 추가
        if total < answer:  # 최소 비용 갱신
            answer = total
        return

    if total >= answer:  # 현재 비용이 최소 비용보다 크면 탐색 중단(가지 치기)
        return

    for next in range(1, N):
        if not visited[next]:  # 방문하지 않은 구역 탐색
            visited[next] = True
            dfs(cnt + 1, next, total + board[now][next])
            visited[next] = False

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    answer = float('inf')

    visited[0] = True  # 시작 구역 방문 처리
    dfs(1, 0, 0)

    print(f"#{test_case} {answer}")