from collections import deque # 큐 사용

#N,L,R 입력 (NxN 크기의 땅, L, R)
n, l ,r = map(int, input().split())

population = []
# 둘째 줄부터 N개의 줄에 각나라의 인구수
for _ in range(n):
    population.append(list(map(int, input().split())))

count = 0 # 인구 이동 횟수
first_check = True # 첫번째 여부 체크
population_check = False # 이동 가능 여부 체크


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y):
    if x < 0 and x >= n and y < 0 and y >= n: # 범위를 벗어 난 경우
        return 

    if open[x][y] == False: # 방문한적 이 없을때,
                open[x][y] = True # 방문 체크

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    add = (population[x][y] + population[nx][ny]) / 2
                    if open[nx][ny] == False and add >= l and add <= r: # 국경 오픈 여부 확인
                        
                        if first_check == True:
                            queue.append((x,y))
                            first_check = False

                        if population_check == False:
                            population_check = True

                        queue.append((nx,ny))
                        dfs(nx,ny)
    

     

while count < 2000:
    
    # 큐 생성
    
    queue = deque()
    open = [[False] * n for _ in range(n)] # 오픈 가능 여부 및 방문 여부 체크

    for i in range(n):
        for j in range(n):
            first_check = True
            if open[i][j] == False:
                dfs(i,j)
                
                queue_r = 0
                queue_c = 0
                while queue:
                    q = queue.appendleft()
                    queue_r += q
                    queue_c += 1
                
    count += 1

    


    
                        


                        
                    
                