import sys
from collections import deque

input=sys.stdin.readline

n,m,v=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]


# 노드 간 인접 행렬 생성 / 인접 행렬 대신 인접 리스트로 선언 시 모든 노드가 아닌 연결된 노드만 확인하므로 더 빨라질 수 있음
for i in range(m):
    s,e=map(int, input().split())
    graph[s][e]=1
    graph[e][s]=1


# DFS 함수
def dfs(v):
    for i in range(1, n+1):
        # 연결된 각 노드에 대해 방문하지 않은 노드가 있는 경우, 재귀로 더 이상 방문할 노드가 없을 때까지 탐색
        if not visited_dfs[i] and graph[v][i]==1:
            visited_dfs[i]=True
            dfs_result.append(i)
            dfs(i)


# BFS 함수
def bfs(v):
    q=deque()
    q.append(v)

    while q:
        curNode=q.popleft()

        # 연결된 각 노드에 대해 방문하지 않은 노드가 있는 경우, 방문 처리 후 덱에 다음 노드 추가함. 더 이상 방문할 노드가 없을 때까지 탐색
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[curNode][i]==1:
                visited_bfs[i]=True
                q.append(i)
                bfs_result.append(i)

# DFS 방문 여부 리스트 visited_dfs 선언
dfs_result=[v]
visited_dfs=[False]*(n+1)
visited_dfs[v]=True
dfs(v)

# BFS 방문 여부 리스트 visited_bfs 선언
bfs_result=[v]
visited_bfs=[False]*(n+1)
visited_bfs[v]=True
bfs(v)

print(" ".join(str(node) for node in dfs_result))
print(" ".join(str(node) for node in bfs_result))