"""
    입력 조건:
    첫째 줄에 공간의 크기를 나타내는 N이 주어진다.(1<=N<=100)
    둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.(1 <= 이동횟수 <= 100)
    출력 조건:
    첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백을 구분하여 출력한다.
"""
'''
# 공간 입력받기
n = int(input())

# 이동 계획 입력받기
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L','R','U','D']

x, y = 1, 1 # 출발 좌표

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > 0 and nx < n+1 and ny > 0 and ny < n+1:
                x , y = nx , ny
            break

print(x, y)
'''

# 공간의 크기 n*n
n = int(input())

# 여행가의 이동 계획
moves = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L','R','U','D']

x, y = 1, 1

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < n+1 and nx > 0 and ny < n+1 and ny > 0:
                x, y = nx, ny
                break

print(x, y)
