def dfs(graph, v, visted):
    # 현재 노드를 방문 처리
    visted[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visted[i]:
            dfs(graph, i, visted)

# 각 노드가 연결된 정보를 리스트 자료형으로 변환

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 변환(1차원 리스트)
visted = [False] * 9

dfs(graph, 1, visted)