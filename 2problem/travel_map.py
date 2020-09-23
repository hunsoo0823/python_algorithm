"""
 입력 조건
    1. 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백을 구분하여 입력한다.(3<=N, M<=50)
    2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A,B)와 바로보는 방향 d가 각각 서로 공백을 구분하여 주어진다.
    방향 d의 값으로는 다음과 같이 4가지가 존재한다.
    3. 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
    맵의 외곽은 항상 바다로 되어 있다.
        - 0 : 육지
        - 1 : 바다
    4. 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
"""

n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]
a, b, dir = map(int, input().split())
d[a][b] = 1
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

stepa = [-1,0,1,0]
stepb = [0,1,0,-1]

count = 0
turn_count = 0

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0

while True:
    turn_left()
    na = a + stepa[dir]
    nb = b + stepb[dir]

    if d[na][nb] == 0 and array[na][nb] == 0:
        d[na][nb] = 1
        a = na
        b = nb
        turn_time = 0
        count += 1
    else:
        turn_time += 1

    if turn_time == 4:
        na = a - stepa[dir]
        nb = b - stepb[dir]
        if array[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_time = 0

print(count)


