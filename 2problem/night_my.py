"""
    첫째 줄에 8 x 8 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
    입력 문자는 a1처럼 옆과 행으로 이루어진다.

    첫번째줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""

input_data = input() # 현재 나이트의 위치 입력받

row = int(input_data[1])
colums = int(ord(input_data[0]))-int(ord('a')) + 1
count = 0

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

# 나이트가 이동가능한지 여부 판단
for i in steps:
    next_row = row + i[0]
    next_colums = colums + i[1]
    # 해당 위치로 이동 가능할시 카운트 증가
    if next_row < 9 and next_row > 0 and next_colums < 9 and next_colums > 0:
        count += 1
    
print(count)
