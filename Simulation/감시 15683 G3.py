import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# board[ny][nx]

def north(board, x, y):
    for i in range(1, y+1):
        ny_ = y - i
        if board[ny_][x] == 0:
            board[ny_][x] = '#'
        elif board[ny_][x] == 6:
            break

def east(board, x, y):
    for i in range(1, M-x):
        nx_ = x + i
        if board[y][nx_] == 0:
            board[y][nx_] = '#'
        elif board[y][nx_] == 6:
            break

def south(board, x, y):
    for i in range(1, N-y):
        ny_ = y + i
        if board[ny_][x] == 0:
            board[ny_][x] = '#'
        elif board[ny_][x] == 6:
            break

def west(board, x, y):
    for i in range(1, x+1):
        nx_ = x - i
        if board[y][nx_] == 0:
            board[y][nx_] = '#'
        elif board[y][nx_] == 6:
            break

# 리턴값 dir을 CCTV가 바라보는 방향으로, 1: 북, 2: 동, 3: 남, 4: 서
def one(board, x, y):
    cases = []
    # 북
    temp = copy.deepcopy(board)
    north(temp, x, y)
    cases.append(temp)
    # 동
    temp = copy.deepcopy(board)
    east(temp, x, y)
    cases.append(temp)
    # 남
    temp = copy.deepcopy(board)
    south(temp, x, y)
    cases.append(temp)
    # 서
    temp = copy.deepcopy(board)
    west(temp, x, y)
    cases.append(temp)
    return cases

def two(board, x, y):
    cases = []
    # 동 & 서
    temp = copy.deepcopy(board)
    east(temp, x, y)
    west(temp, x, y)
    cases.append(temp)
    # 북 & 남
    temp = copy.deepcopy(board)
    north(temp, x, y)
    south(temp, x, y)
    cases.append(temp)
    return cases

def three(board, x, y):
    cases = []
    # 북 & 동
    temp = copy.deepcopy(board)
    north(temp, x, y)
    east(temp, x, y)
    cases.append(temp)
    # 동 & 남
    temp = copy.deepcopy(board)
    east(temp, x, y)
    south(temp, x, y)
    cases.append(temp)
    # 남 & 서
    temp = copy.deepcopy(board)
    south(temp, x, y)
    west(temp, x, y)
    cases.append(temp)
    # 서 & 북
    temp = copy.deepcopy(board)
    west(temp, x, y)
    north(temp, x, y)
    cases.append(temp)
    return cases

def four(board, x, y):
    cases = []
    # 북 & 동 & 서
    temp = copy.deepcopy(board)
    north(temp, x, y)
    east(temp, x, y)
    west(temp, x, y)
    cases.append(temp)
    # 북 & 동 & 남
    temp = copy.deepcopy(board)
    north(temp, x, y)
    east(temp, x, y)
    south(temp, x, y)
    cases.append(temp)
    # 동 & 남 & 서
    temp = copy.deepcopy(board)
    east(temp, x, y)
    south(temp, x, y)
    west(temp, x, y)
    cases.append(temp)
    # 남 & 서 & 북
    temp = copy.deepcopy(board)
    south(temp, x, y)
    west(temp, x, y)
    north(temp, x, y)
    cases.append(temp)
    return cases

def five(board, x, y):
    temp = copy.deepcopy(board)
    north(temp, x, y)
    east(temp, x, y)
    south(temp, x, y)
    west(temp, x, y)
    return [temp]

# CCTV 위치 기록
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((j, i, board[i][j]))

# 백트래킹으로 모든 경우의 수 탐색
def dfs(idx, board):
    global min_blind
    
    if idx == len(cctvs):
        # 사각지대 개수 세기
        blind = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    blind += 1
        min_blind = min(min_blind, blind)
        return
    
    x, y, cctv_type = cctvs[idx]
    
    # CCTV 종류에 따라 가능한 모든 방향 시도
    if cctv_type == 1:
        cases = one(board, x, y)
    elif cctv_type == 2:
        cases = two(board, x, y)
    elif cctv_type == 3:
        cases = three(board, x, y)
    elif cctv_type == 4:
        cases = four(board, x, y)
    elif cctv_type == 5:
        cases = five(board, x, y)
    
    for case in cases:
        dfs(idx + 1, case)

min_blind = N * M
dfs(0, board)
print(min_blind)
