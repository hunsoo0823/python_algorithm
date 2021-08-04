def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 수 n, 여행 계획 도시수 m
n, m = map(int, input().split())

# 각 도시에서 이동할 수 있는 경로를 담을 리스트
city_graph = []

parent = [0] * (n+1)

# 부모노드 초기화
for i in range(1, n+1):
    parent[i] = i

# 도시 경로 입력받기
for _ in range(n):
    city_graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i, n):
        if city_graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

route = list(map(int, input().split()))

# 모든 부모노드가 같아야 루트 생성 가능
check = parent[route[0]]

result = True

for i in range(1, m):
    if parent[i] != check:
        result = False

if result == True:
    print('Yes')
else:
    print('No')