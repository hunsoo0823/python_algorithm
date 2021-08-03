# 여행지의 수 n, 여행 계획 도시수 m
n, m = map(int, input().split())

city_graph = []
for _ in range(n):
    city_graph.append(list(map(int, input().split())))

print(city_graph)