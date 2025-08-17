from collections import deque
import sys

"""
input = sys.stdin.readline를 했을 때 실행 시간이 더 짧은 이유:
일반 input()은 프롬프트 출력 + 개행문자 '\n' 제거의 역할을 해서 느리지만,
sys.stdin.readline을 적용하면 C언어처럼 프롬프트를 출력하지 못하고, 개행문자도 제거하지 않아 빠름

그렇다면...
sys.stdin.readline을 적용한 코드와 그렇지 않은 코드에 split()을 적용했는데 왜 결과가 동일한가?
split() 함수는 문자열의 맨 앞, 뒤의 공백과 개행문자를 자동으로 무시하기 때문

그러니까!
input = sys.stdin.readline을 사용하자
"""
input = sys.stdin.readline

box = []    # 토마토 상자
m,n = map(int, input().split())

for _ in range(n):
    box.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

day = [[0]*m for _ in range(n)] # 토마토가 다 익는 데 걸릴 날짜를 저장할 이중 리스트, 기본값 0

def bfs():
    q = deque()

    # 토마토 상자의 초기 상태에서 익은 토마토의 위치 확인 후 큐에 append
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i,j))

    while q:
        curX, curY = q.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny]==0:  # 익은 토마토 옆에 익을 수 있는 토마토가 있는 경우 / 다음 토마토가 익을 수 있는 경우에만 진행하므로 visited 이중 리스트 만들 필요 X
                q.append((nx,ny))
                box[nx][ny] = 1
                day[nx][ny] = day[curX][curY] + 1

bfs()   # BFS 수행

# day 리스트에서 가장 큰 값(토마토가 다 익는 데 걸린 날) 탐색 후 출력
# 만약 안 익은 토마토가 있으면 -1 출력 후 종료
result = 0
for i in range(n):
    for j in range(m):
        result = max(result, day[i][j])
        if box[i][j] == 0:
            print(-1)
            exit()

print(result)