"""
  - 입력조건
    - 첫번째 줄에 두정수 N,M(4<=N, M<=200)이 주어집니다.
    다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
    각각의 수들은 공백없이 붙어서 입력으로 제시된다. 또한 시작칸과 마지막칸은 항상 0이다.
  - 출력조건
    첫째 줄에 최소 이동 칸의 개수를 출력한다.
"""
# n * m을 입력받음
from collections import deque

n, m = map(int, input().split())

mapping = []
for i in range(n):
    mapping.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            if mapping[nx][ny] == 1:
                queue.append((nx,ny))
                mapping[nx][ny] = mapping[x][y] + 1

bfs(0,0)

print((mapping[n-1][m-1]))