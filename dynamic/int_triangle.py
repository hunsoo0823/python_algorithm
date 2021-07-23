# 삼각형의 크기 n
n = int(input())

# 정수 삼각형
array_tri = []
for i in range(n):
    array_tri.append(list(map(int, input().split())))

#array_tri = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
array_temp = []

# 합을 저장할 삼각형 초기화
array_temp.append(array_tri[0])
for i in range(1,n):
    temp = [0] * (i+1)
    array_temp.append(temp)

# 왼쪽아래, 오른쪽 아래
dx = [1,1]
dy = [0,1]

# 삼각형의 위치마다 최대합 구하기
for x in range(n-1):
    for y in range(x+1):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            array_temp[nx][ny] = max(array_temp[nx][ny], array_tri[nx][ny] + array_temp[x][y])
    
# 첫번째줄에 합이 최대가 되는 값 반환
max_value = max(array_temp[n-1])
print(max_value)
            