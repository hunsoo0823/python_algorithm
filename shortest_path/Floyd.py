# 도시의 개수 (1<=n<=100)
n = int(input())

# 버스의 개수 (1<=m<=100,000)
m = int(input())

INF = 1e5

city_array = [[INF] * (n+1) for _ in range(n+1)]

# m개의 버스정보 입력(버스 시작도시 a, 버스 도착도시 b, 비용 c)
for _ in range(m):
    a, b ,c = map(int , input().split())
    city_array[a][b] = min(city_array[a][b], c)

for i in range(1, n+1):
    for j in range(1,n+1):
        if i == j:
            city_array[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            city_array[i][j] = min(city_array[i][j], city_array[i][k]+city_array[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if city_array[i][j] == INF:
            print(0, end=" ")
        else:
            print(city_array[i][j], end=" ")
    print()