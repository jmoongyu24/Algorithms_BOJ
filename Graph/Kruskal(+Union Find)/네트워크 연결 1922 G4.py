"""
크루스칼 알고리즘: 가장 적은 비용으로 모든 노드를 연결하는 MST 알고리즘 중 하나
핵심 아이디어: 간선을 비용이 적은 순서대로 그래프에 포함시키자
단, 포함시키는 과정에서 사이클이 발생하면 안 됨

그래프에 포함시킬지 말지 결정하는 과정에서 '유니온-파인드' 알고리즘 사용
"""

import sys
input = sys.stdin.readline

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    # 더 작은 노드의 값을 부모로 설정
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드의 부모와 노드의 값이 다르면 노드의 부모의 부모를 찾으러 재귀 호출
# ex: 노드 7의 부모가 1이라면, parent[7] != 7이므로 7의 부모인 1의 부모를 찾기 위해 재귀 호출 진행
def find_parent(x):
    # 노드의 부모와 노드의 값이 같으면 그대로 return
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    # 노드의 부모와 노드의 값이 다르면 부모의 부모를 찾으러 재귀 호출
    return parent[x]

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]
network = []    # 크루스칼 알고리즘은 모든 간선 정보를 하나의 단일 리스트로 저장함
                # network = [[] for _ in range(N+1)] 형태 X

for _ in range(M):
    a, b, c = map(int, input().split())
    network.append((a, b, c))

network.sort(key=lambda x: x[2])    # 비용 기준 정렬
cost = 0

for edge in network:    # 정렬된 모든 간선을 순차적으로 탐색하면서 유니온-파인드로 연결
    a, b, c = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cost += c

print(cost)