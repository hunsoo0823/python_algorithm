# 부모 노드를 찾는 함수
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


# 탑승구의 수 G
g = int(input())

# 비행기의 수 P
p = int(input())

airplane = [0] * p
# p개의 줄에 비행기가 도킹할 수 있는 탑승구의 정보
for i in range(p):
    airplane[i] = int(input())

# 부모노드 자기자신으로 초기화
parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

i = 0
while i < p:
    index = airplane[i]
    print(index)

    if parent[index] == index: # 토킹 장소가 비어있을때,
        union_parent(parent, index, index-1)
    elif parent[index] != 0: # 루트 노드가 아닐때 즉 비행기를 더 도킹할 수 있는 상태
        union_parent(parent, parent[index], parent[index]-1)
    else:
        break

    i += 1

print(i)