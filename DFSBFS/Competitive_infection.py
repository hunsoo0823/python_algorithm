import copy

# n,k (N*N 시험관, 1~K번까지 K가지의 바이러스 1<=n<=200, 1<=k<=1,000)
n, k = map(int, input().split())

# N개의 줄에 걸쳐서 시험관 정보
tube = []
for _ in range(n):
    input_tube = list(map(int, input().split()))
    tube.append(input_tube)

# s,x,y (s초, x,y 좌표)
s, x, y = map(int, input().split())

# 동, 서, 남, 북 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def virus(virus_num):
    tube_temp = copy.deepcopy(tube)

    for i in range(n):
        for j in range(n):
            if tube[i][j] == virus_num:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx > -1 and nx < n and ny > -1 and ny < n: # 범위를 벗어났는지 확인
                        if tube[nx][ny] == 0: # 빈 공간일 때 바이러스 전파
                            tube_temp[nx][ny] = virus_num

    for i in range(n):
        for j in range(n):
            tube[i][j] = tube_temp[i][j]
    
def dfs(time):
    while time <= s:
        for virus_num in range(1, k+1):
            virus(virus_num) # 바이러스 순서대로 바이러스 전파
        time += 1

    return tube[x-1][y-1]
        

time = 1

result = dfs(time)

for t in tube:
    print(t)

print(result)