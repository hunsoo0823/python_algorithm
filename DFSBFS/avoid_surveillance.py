from collections import deque

# n x n 크기의 복도 (3<=n<=6)
n = int(input())

# 선생님 위치 좌표
teacher = []
output = False

# 선생님 감시 위치(1칸)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 둘째 줄부터 N개의 줄에 걸쳐서 복도의 정보
# 각 행에서는 N개의 원소, 공백으로 구분
# 해당 위치에 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X (X>=3)
school = [] 

for i in range(n):
    input_map = list(input().split()) # 복도의 정보 입력
    school.append(input_map)
    for j in range(n):
        if school[i][j] == 'T':
            # 선생님의 좌표 x, 좌표 y
            teacher.append((i,j))

def bfs():
    # 큐 생성
    q = deque()

    for t in teacher:
        for i in range(4):
            q.append((t[0], t[1], i)) # 좌표 x, y, 바라보는 방향 

    # 큐가 빌 때까지 반복
    while q:
        x, y, dir = q.popleft()
        
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx >= 0 and nx < n and ny >= 0 and ny < n: # 범위 를 벗어나지 않았을 때
            if school[nx][ny] == 'O': # 벽에 마주첬을 때
                continue
            elif school[nx][ny] == 'S': # 학생을 마주첬을 때
                return False # False 반환
            elif school[nx][ny] == 'X': # 빈공간일때, 그 방향으로 감시 확대
                q.append((nx, ny, dir))

    # 학생을 감지하지 못했을때 True 반환
    return True

def dfs(count):
    # 글로벌 전역변수 output
    global output

    # 학생들이 모두 발각되지 않은 경우를 발견되었을 때는 중지
    if output == True:
        return 

    # 벽 세개를 다 첬을시
    if count == 3:
        for s in school:
            print(s)
        print()

        result = bfs()
        if result == True:
            output = True
        return

    for i in range(n):
        for j in range(n):
            if school[i][j] == 'X':
                school[i][j] = 'O'
                count += 1
                dfs(count)
                school[i][j] = 'X'
                count -= 1

count = 0

dfs(count)

if output == True:
    print("YES")
else:
    print("NO")
                
        






