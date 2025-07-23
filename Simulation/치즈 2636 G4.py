from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

row, col=map(int, input().split())
square=[list(map(int,input().split())) for _ in range(row)]

hour=0
before_1hour=0

def air_out(x,y):
    q=deque()
    visited=[[False]*col for _ in range(row)]

    # 바깥 공기와 치즈 내부 공기와 구분하기 위해 바깥 공기는 -1 처리 / 치즈 녹기 전까지 내부 공기는 0으로 유지
    square[x][y]=-1
    visited[x][y]=True
    q.append((x,y))

    while q:
        curX, curY=q.popleft()

        for i in range(4):
            nx=curX+dx[i]
            ny=curY+dy[i]

            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and square[nx][ny]==0:
                square[nx][ny]=-1
                visited[nx][ny]=True
                q.append((nx,ny))

def count_cheese():
    cheese_cnt=0
    for i in range(row):
        for j in range(col):
            if square[i][j]==1:
                cheese_cnt+=1
    return cheese_cnt

def check_air_adjacent_cheese():
    for i in range(row):
        for j in range(col):
            if square[i][j]==1:
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<row and 0<=ny<col and square[nx][ny]==-1:
                        square[i][j]=2
                        break
    
    for i in range(row):
        for j in range(col):
            if square[i][j]==2:
                square[i][j]=-1

def melt_cheese():
    # 1. 치즈 전체 순회하면서 총 치즈 개수 세기 - 만약 치즈가 1조각이라도 없으면 종료
    # 2. 치즈 전체 순회하면서 바깥 공기와 인접한 치즈 체크
    # 2. 치즈 녹이고 다시 반복
    while count_cheese()>0:
        before_1hour=count_cheese()
        hour+=1
        check_air_adjacent_cheese()

melt_cheese()

print(hour)
print(before_1hour)