from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)    # indegree 테이블

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # A가 B보다 앞에 있어야 하므로 A -> B 방향으로 간선 추가
    indegree[B] += 1

def topological_sort():
    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:    # indegree가 0인 노드를 모두 큐에 추가
            q.append(i)
        
    while q:
        curNode = q.popleft()
        result.append(curNode)

        for nextNode in graph[curNode]:
            indegree[nextNode] -= 1 # 현재 노드와 연결된 모든 다음 노드들의 indegree 1 감소

            if indegree[nextNode] == 0: # indegree가 0이 되었다면 큐에 추가
                q.append(nextNode)

    return result

print(' '.join(map(str, topological_sort())))