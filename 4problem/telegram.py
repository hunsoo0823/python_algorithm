"""
    - 입력조건
     - 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
     (1 <= N <= 30,000 , 1 <= M <= 200,000, 1 <= C <= N)
     - 둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다. 이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며,
     메시지 전달되는 시간이 Z라는 의미다.
     (1 <= X, Y <= N, 1<= Z <= 1,000)
     - 출력조건
      - 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
"""
import heapq
import sys

INF = int(1e9)
# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, c = map(int, sys.stdin.readline().split())
# 시작 지점
start = c
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받긷
for _ in range(m):
    x, y, z = map(int,sys.stdin.readline().split())
    graph[x].append((y,z))

def dijkstart(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q , (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        # 연결 되어 있는 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

print(distance)
count = 0
max_distance = 0
for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance, i)

print(count - 1 , max_distance)




