import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def north(board, x, y):
    for i in range(0, y):
        if board[i][x] == 0:
            board[i][x] = '#'
        elif board[i][x] == 6:
            break

def east(board, x, y):
    for i in range(x+1, M):
        if board[y][i] == 0:
            board[y][i] = '#'
        elif board[y][i] == 6:
            break

def south(board, x, y):
    for i in range(y+1, N):
        if board[i][x] == 0:
            board[i][x] = '#'
        elif board[i][x] == 6:
            break

def west(board, x, y):
    for i in range(0, x):
        if board[y][i] == 0:
            board[y][i] = '#'
        elif board[y][i] == 6:
            break

# 리턴값 dir을 CCTV가 바라보는 방향으로, 1: 북, 2: 동, 3: 남, 4: 서
def one(board, x, y):
    cases = []
    # 북 방향 모두 #으로 채우고 append
    tmp = copy.deepcopy(board)
    north(tmp, x, y)
    cases.append(tmp)
    # 동
    tmp = copy.deepcopy(board)
    east(tmp, x, y)
    cases.append(tmp)
    # 남
    tmp = copy.deepcopy(board)
    south(tmp, x, y)
    cases.append(tmp)
    # 서
    tmp = copy.deepcopy(board)
    west(tmp, x, y)
    cases.append(tmp)

    return cases

def two(board, x, y):
    cases = []
    # 동 & 서
    tmp = copy.deepcopy(board)
    east(tmp, x, y)
    west(tmp, x, y)
    cases.append(tmp)
    # 북 & 남
    tmp = copy.deepcopy(board)
    north(tmp, x, y)
    south(tmp, x, y)
    cases.append(tmp)

    return cases

def three(board, x, y):
    cases = []
    # 북 & 동
    tmp = copy.deepcopy(board)
    north(tmp, x, y)
    east(tmp, x, y)
    cases.append(tmp)
    # 동 & 남
    tmp = copy.deepcopy(board)
    east(tmp, x, y)
    south(tmp, x, y)
    cases.append(tmp)
    # 남 & 서
    tmp = copy.deepcopy(board)
    south(tmp, x, y)
    west(tmp, x, y)
    cases.append(tmp)
    # 서 & 북
    tmp = copy.deepcopy(board)
    west(tmp, x, y)
    north(tmp, x, y)
    cases.append(tmp)

    return cases

def four(board, x, y):
    cases = []
    # 북 & 동 & 서
    tmp = copy.deepcopy(board)
    north(tmp, x, y)
    east(tmp, x, y)
    west(tmp, x, y)
    cases.append(tmp)
    # 북 & 동 & 남
    tmp = copy.deepcopy(board)
    north(tmp, x, y)
    east(tmp, x, y)
    south(tmp, x, y)
    cases.append(tmp)
    # 동 & 남 & 서
    tmp = copy.deepcopy(board)
    east(tmp, x, y)
    south(tmp, x, y)
    west(tmp, x, y)
    cases.append(tmp)
    # 남 & 서 & 북
    tmp = copy.deepcopy(board)
    south(tmp, x, y)
    west(tmp, x, y)
    north(tmp, x, y)
    cases.append(tmp)

    return cases

def five(board, x, y):
    tmp = copy.deepcopy(board)
    north(tmp, x, y)
    east(tmp, x, y)
    south(tmp, x, y)
    west(tmp, x, y)

    return [tmp]

# CCTV 위치, 종류 저장
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv.append((j, i, board[i][j]))

def dfs(idx, board):
    global min_blind
    
    # 모든 카메라 설치 완료, 사각지대 수 계산
    if idx == len(cctv):
        blind = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    blind += 1
        min_blind = min(min_blind, blind)

        return
    
    x, y, cctv_type = cctv[idx]
    
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
    
    # cases에는 각 방향별로 감시가 끝난 보드 상태들이 들어있고, 그 중 하나를 선택해서 다음 cctv로 넘어감. 모든 경우 시도함
    for case in cases:
        dfs(idx + 1, case)

min_blind = N * M
dfs(0, board)
print(min_blind)