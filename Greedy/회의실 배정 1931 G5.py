import sys
input = sys.stdin.readline

N = int(input())

meeting = []

for _ in range(N):
    s, e = map(int, input().split())
    meeting.append((e,s))

# 종료 시각으로 오름차순 정렬 후 종료 시각이 같으면 시작 시각으로 오름차순 정렬
meeting.sort(key=lambda x:(x[0], x[1]))
cur_end = meeting[0][0]
cnt = 1

for i in range(1, N):
    e, s = meeting[i]
    if s >= cur_end:
        cur_end = e
        cnt += 1

print(cnt)