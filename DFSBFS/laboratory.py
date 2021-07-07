
# 지도의 세로의 크기 N, 가로크기 M(3<=N, M<=8)
n, m = map(int, input().split())

result = 0
count = 0
temp_map = [[0]* m for _ in range(n)] # 스코어 계산을 위해 사용될 맵
graph_map = [] # 오리지널 맵

# 동, 서, 남, 북 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 지도의 모양 (0 빈칸, 1 벽, 2 바이러스)
for _ in range(n):
    shape = list(map(int, input().split()))
    graph_map.append(shape)

# 바이러스를 전파 시키는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2
                virus(nx,ny)

# 스코어 계산하는 함수
def get_socore():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                score += 1

    return score

def dfs(count):
    global result
    # 벽 세개를 다 첬을시
    if count == 3:
        # 임시 맵으로 복사
        for i in range(n):
            for j in range(m):
                temp_map[i][j] = graph_map[i][j]
        # 바이러스 발견시 전파
        for i in range(n):
            for j in range(m):
                if temp_map[i][j] == 2:
                    virus(i, j)
        
        result = max(result, get_socore())
        return

    for i in range(n):
        for j in range(m):
            if graph_map[i][j] == 0:
                graph_map[i][j] = 1
                count += 1
                dfs(count)
                graph_map[i][j] = 0
                count -= 1

dfs(0)
print(result)