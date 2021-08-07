# 부모노드를 찾는 함수
def find_parent(parent ,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 집합에 포함 시키는 함수
def union_parent(parnet, a, b):
    a = find_parent(parent, a)
    b = find_parent(parnet, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 행성의 갯수 n
n = int(input())

planet_ = []
# 각 행성의 x,y,z 좌표
for _ in range(n):
    x, y, z = map(int, input().split())
    planet_.append((x,y,z))

# 부모노드 생성 및 초기화
parent = [0] * (n+1)
for i in range(n):
    parent[i] = i

# 각 행성 사이의 거리와, x좌표를 넣을 변수
planet_cost_x = []

for i in range(n):
    for j in range(i+1, n):
        cost = min(abs(planet_[i][0]-planet_[j][0]), abs(planet_[i][1]-planet_[j][1]), abs(planet_[i][2]-planet_[j][2]))
        planet_cost_x.append((cost, i, j))

planet_cost_x.sort()

distance = 0

for planet in planet_cost_x:
    cost, a, b = planet
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        distance += cost
        
print(distance)