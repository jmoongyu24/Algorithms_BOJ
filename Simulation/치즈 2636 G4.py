from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

row, col=map(int, input().split())
cheese=[list(map(int, input().split())) for _ in range(row)]

def bfs():
    q=deque([(0, 0)])
    visited=[[False]*col for _ in range(row)]
    visited[0][0]=True

    # 치즈가 녹을 위치를 저장할 큐
    to_be_melted=deque()

    while q:
        curX, curY=q.popleft()

        for i in range(4):
            nx=curX+dx[i]
            ny=curY+dy[i]

            # 맵을 벗어나지 않았고, 방문하지 않은 경우
            if 0<=nx<row and 0<=ny<col and not visited[nx][ny]:
                visited[nx][ny] = True

                # 치즈가 없는 경우 큐에 추가
                if cheese[nx][ny]==0:
                    q.append((nx, ny))
                # 치즈가 있는 경우 녹을 위치에 추가. 나중에 한번에 녹임
                elif cheese[nx][ny]==1:
                    to_be_melted.append((nx, ny))
    
    # 녹을 치즈 한번에 녹임
    for x, y in to_be_melted:
        cheese[x][y]=0

    return len(to_be_melted)

# 초기 전체 치즈 개수 카운트
cnt=sum(sum(line) for line in cheese)
time=1

while True:
    visited=[[False]*col for _ in range(row)]
    melt_cnt=bfs()
    cnt-=melt_cnt

    # 치즈가 모두 녹았을 경우 종료
    if cnt==0:
        print(time)
        print(melt_cnt)
        break

    time+=1