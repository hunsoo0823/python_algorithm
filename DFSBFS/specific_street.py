from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

# 도시의 개수 만큼 연결된 맵 초기화
array_road = [[] for _ in range(n+1)]
visted = [False] * (n+1)
distance = [0] * (n+1)

# A->B로 이동하는 단방향 도로
for _ in range(m):
    a, b = map(int, input().split())
    array_road[a].append(b)

def bfs(visted, x, graph):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([x])

    visted[x] = True

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visted[i]:
                distance[i] = distance[v] + 1
                queue.append(i)
                visted[i] = True

bfs(visted, x, array_road)
print(distance)

# 조건에 맞는 거리가 없는지 체크하는 변수
nothing = 0

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
    else:
        nothing += 1

if nothing == n:
    print(-1)