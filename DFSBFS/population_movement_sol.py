from collections import deque

# 땅의크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)을 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    untied = []
    untied.append((x,y))

    # 너비 우선탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))

    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx and 0 <= ny and union[nx][ny] == -1:
                # 옆의 있는 나라의 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y] <= r):
                    q.append((nx,ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1

    # 연합 국가끼리 인구를 분해
    for i, j in untied:                
