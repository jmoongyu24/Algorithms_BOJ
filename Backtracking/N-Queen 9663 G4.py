n = int(input())
cnt = 0

isused1 = [False] * 40  # column을 차지하고 있는지  4x4 기준 4개 사용
isused2 = [False] * 40  # / 방향 대각선을 차지하고 있는지   4x4 기준 7개 사용
isused3 = [False] * 40  # \ 방향 대각선을 차지하고 있는지   4x4 기준 7개 사용

def n_queens(cur):
    global cnt
    if cur == n:  # N개의 퀸 놓는 데 성공
        cnt += 1
        return
    for i in range(n):
        if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:  # column이나 대각선 라인에 퀸이 이미 있으면 넘어감
            continue
        isused1[i] = True
        isused2[i + cur] = True
        isused3[cur - i + n - 1] = True
        n_queens(cur + 1)
        isused1[i] = False
        isused2[i + cur] = False
        isused3[cur - i + n - 1] = False

n_queens(0)
print(cnt)