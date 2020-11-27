"""
 입력 조건
    1. 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백을 구분하여 입력한다.(3<=N, M<=50)
    2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A,B)와 바로보는 방향 d가 각각 서로 공백을 구분하여 주어진다.
    방향 d의 값으로는 다음과 같이 4가지가 존재한다.
        - 0 : 북쪽
        - 1 : 동쪽
        - 2 : 남쪽
        - 3 : 서쪽
    3. 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
    맵의 외곽은 항상 바다로 되어 있다.
        - 0 : 육지
        - 1 : 바다
    4. 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
"""

# 맵의 크기 입력 받기
n, m = map(int , input().split())

d = [[0] * m for _ in range(n)]
# 좌표 및 바라보는 위치 입력받기
a, b ,dir = map(int, input().split())
d[a][b] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북쪽, 동쪽, 남쪽, 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir < 0:
        dir = 3

count = 1 # 몇곳을 방문했는지 확인
turn_time = 0 # 회전 수

while True:
    # 왼쪽으로 회전
    turn_left()

    nx = a + dx[dir]
    ny = b + dy[dir]

    if d[nx][ny] != 1 and array[nx][ny] != 1:
        d[nx][ny] = 1
        a, b = nx , ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = a - dx[dir]
        ny = b - dy[dir]

        if array[nx][ny] == 0:
            a , b = nx, ny
        else:
            break
        turn_time = 0

print(count)




