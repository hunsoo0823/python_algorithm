def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parnet, a, b):
    a = find_parent(parnet, a)
    b = find_parent(parnet, b)
    if a < b:
        parnet[b] = a
    else:
        parnet[a] = b

# 집의 수 n, 도로의 수 m
n, m = map(int, input().split())

all_cost = 0

# 연결되 도로와 거리 입력받기
road_array = []
for _ in range(m):
    x, y, cost = map(int ,input().split())
    road_array.append((cost, x, y))
    all_cost += cost

# 길을 오름차순으로 정렬
road_array.sort()

# 부모노드 그래프
parent = [0] * n
for i in range(n):
    parent[i] = i

# 가로등 비용 계산할 변수
result = 0

for road in road_array:
    cost, x, y = road
    # 사이클이 발생하지 않는다면, 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(all_cost - result)