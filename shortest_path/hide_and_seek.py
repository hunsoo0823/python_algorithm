import heapq
import sys
input = sys.stdin.readline

# 헛간의 갯수 n, 통로의 갯수 m개
n, m = map(int, input().split())

INF = int(1e9)
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 서로 연결된 두 헛간 A,B
hide = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    hide[a].append(b)
    hide[b].append(a)

def dijkstra(start):
    q = [] 
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in hide[now]:
            cost = dist + 1
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

start = 1
#다익스트라 알고리즘 수행
dijkstra(start)

"""
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우
    else:
        print(distance[i])
"""
min_distance = 0
index = 0
for i in range(2, n+1):
    if min_distance < distance[i]:
        min_distance = distance[i]
        index = i

print(index, min_distance, distance.count(min_distance))