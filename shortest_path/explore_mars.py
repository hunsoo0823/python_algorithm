INF = 100
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# dfs함수
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        result_array[nx][ny] = min(result_array[nx][ny], array_mars[nx][ny] + result_array[x][y])

        #for re in result_array:
        #   print(re)
        
        print(nx, ny)
        dfs(nx,ny)

# 테스트 케이스의 수 입력받기
for i in range(int(input())):
    
    # 탐사 공간의 크기 n
    n = int(input())
    
    array_mars = []
    for i in range(n):
        array_mars.append(list(map(int, input().split())))

    # 결과를 저장할 맵
    result_array = [[INF] * n for _ in range(n)]
    result_array[0][0] = array_mars[0][0]

    dfs(0, 0)
    

