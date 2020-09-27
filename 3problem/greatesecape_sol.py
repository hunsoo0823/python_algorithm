from collections import deque

# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때 까
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #우 공간을 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우
            if graph[nx][ny] == 0:
                continue
            # 첫방문인 경우 최단거리 기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n - 1][m - 1]

print(bfs(0,0))