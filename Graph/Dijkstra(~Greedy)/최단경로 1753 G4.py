"""
다익스트라 알고리즘은 현재 방문한 노드에서 자신과 연결된 노드와의 거리 중 가장 짧은 노드를 선택하여
'한 점에서 다른 모든 점까지의 최단거리'를 구하는 일종의 '그리디 알고리즘'

우선순위 큐를 쓰는 알고리즘 시간복잡도: O(ElogE) / 간선 당 최대 1개의 노드가 추가되기 때문
만약 E가 V^2에 가까운 경우 우선순위 큐를 쓰지 않는게 O(V^2+E)로 더 빠르지만, 보통 V를 매우 크게 두는 문제가 많아 우선순위 큐를 써도 무방함

우선순위큐(or 힙)에 거리가 가장 짧은 노드를 선택할 수 있게 하고,
최단 거리 테이블에 시작 지점부터 각 노드까지의 최단 거리를 기록함

1.  우선순위 큐에 (0, 시작점) 추가
2.  우선순위 큐에서 거리가 가장 짧은 노드 선택, 해당 거리가 최단 거리 테이블에 있는 값과 같으면 3번 수행
    그렇지 않으면 4번 수행
3.  현재 노드에서 가리키는 다음 노드를 v라고 할 때, v와 이웃한 노드들에 대해 최단 거리 테이블 값보다
    v를 거쳐가는 것이 더 작은 값을 가질 경우 최단 거리 테이블의 값을 갱신하고
    우선순위 큐에 (거리, 이웃한 정점의 번호) 추가
4. 우선순위 큐가 빌 때까지 2~3 반복
"""

import heapq
import sys

INF = 987654321
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [INF] * (V+1)    # 각 노드 별 거리 초기화

def dijkstra(start):
    hq=[]
    heapq.heappush(hq, (0, start)) # (거리, 노드) 형태로 힙에 삽입

    dist[start] = 0                 # 시작 노드 거리 0으로 초기화

    while hq:
        curDist, curNode = heapq.heappop(hq)

        # 현재 꺼낸 노드의 거리가 최단거리 테이블[현재노드]에 기록된 값보다 크면 스킵
        if dist[curNode] < curDist:
            continue

        # 현재 노드와 연결된 다른 노드 순회 탐색
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리 계산
        # nextNode[0]: 다음 노드 v
        # nextNode[1]: 현재 노드에서 다음 노드로의 가중치 w
        for nextNode in graph[curNode]:
            nextDist = curDist + nextNode[1]    

            # 만약 '다음 노드로의 거리'가 최단거리 테이블의 '다음 노드로의 거리'값보다 작으면 업데이트
            if nextDist < dist[nextNode[0]]:
                dist[nextNode[0]] = nextDist
                heapq.heappush(hq, (nextDist, nextNode[0]))

if __name__ == "__main__":
    dijkstra(K)

    for i in range(1, V+1):
        if dist[i] == INF:
            print("INF")
        else: print(dist[i])