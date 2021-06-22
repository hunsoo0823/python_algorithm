
# 보드의 크기 N*N
n = int(input())
array_map = [[0] * n for _ in range(n)]

# 사과의 갯수 K개
k = int(input())

# 각 사과의 위치
for _ in range(k):
    x, y = map(int, input().split())
    #사과가 있는 위치는 2로 지정
    array_map[x-1][y-1] = 2

# 뱀의 방향 변환 횟수 L
L = int(input())

array_turn = []

for _ in range(L):
    X, C = input().split()
    array_turn.append((int(X),C))

time_count = 0
# 0 : right , 1: down, 2: left, 3: up
# 오른쪽 방향을 바라보고 시작
direction = 0
# right, down, left, up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn_right():
    global direction
    direction += 1
    if direction > 3:
        direction = 0
    print("오른쪽으로 회전합니다")

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3
    print("왼쪽으로 회전합니다.")

# 회전 초기화
turn_time = 0
turn_count = array_turn[turn_time][0]

# 초기 머리 좌표
x, y = 0, 0

# 처음 지렁이 위치
array_map[x][y] = 1
dummy = [(x,y)]

while True:
    time_count += 1

    # 지렁이 방향에 따라 움직임 
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx > (n-1) or ny < 0 or ny > (n-1):
        print("벽")
        break
    elif array_map[nx][ny] == 1:
        print("몸통")
        break
    else:
        if array_map[nx][ny] == 2:
            array_map[nx][ny] = 1
            dummy.append((nx, ny))
        else:
            array_map[nx][ny] = 1
            tx, ty = dummy.pop(0)
            print(tx, ty)
            array_map[tx][ty] = 0
            dummy.append((nx, ny))

    x, y = nx, ny
    # 회전 시간이 되었을때 회전
    if turn_time < L and time_count == turn_count:
        if array_turn[turn_time][1] == 'L':
            turn_left()
        else:
            turn_right()
        turn_time += 1
        if turn_time < L:
            turn_count = array_turn[turn_time][0]

    for map in array_map:
        print(map)
    print()

print(time_count)

    
