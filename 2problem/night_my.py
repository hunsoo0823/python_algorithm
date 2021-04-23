"""
    첫째 줄에 8 x 8 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
    입력 문자는 a1처럼 옆과 행으로 이루어진다.

    첫번째줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""
"""
# 좌표 입력받기
coordinate = input()
# 위치 변환
row = int(coordinate[1])
column = int(ord(coordinate[0])) - int(ord('a')) +1
count = 0 # 경우의 수 계산

# step 8가지 (나이트가 움직일 수 있는 경우의 수)
dx = [-2, -2, 2, 2, -1, 1, 1, -1 ]
dy = [-1, 1, 1, -1, -2, -2, 2, 2 ]

for i in range(7+1):
    nx = row + dx[i]
    ny = column + dy[i]
    if nx > 0 and nx < 8+1 and ny > 0 and ny < 8+1:
        count += 1

print(count)
"""

# 좌표 입력받기
coordinate = input()

# 위치 변환
row = int(coordinate[1])
column = int(ord(coordinate[0])) - int(ord('a')) +1

steps = [(-2,-1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row > 0 and next_column < 9 and next_column > 0 and next_column < 9:
        result += 1

print(result)