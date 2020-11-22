"""
    입력조건
        - 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2이상 100,000 이하인 정수이고, M은 1이상 1,000,000 이하인 정수이다.
        - 그다음 줄부터 M줄에 걸쳐 길의 정보가 A,B,C 3개의 정수로 공백으로 구분되어 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C(1<=C<=1,000)라는 뜻이다.
    출력조건
        - 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소의 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

edges = []
result = 0

# 부모 테이블상ㅇ데서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int , input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a ,b)
        result += cost
        last = cost

print(result-last)