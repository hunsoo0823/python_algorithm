from itertools import combinations

#n, m 의 값 입력 (n은 n*n의 도시의 크기, m의 최소 치킨집의 개수)
n, m = map(int, input().split())

# 도시의 정보(0은 빈공간, 1은 집, 2 치킨집)
# 집의 개수는 2n을 넘기지 않고, m은 13보다 작거나 같습니다.
house, chicken = [] , []

for x in range(n):
    city = list(map(int, input().split()))
    for y in range(n):
        if city[y] == 1:
            house.append((x,y)) # 일반 집
        elif city[y] == 2:
            chicken.append((x,y)) # 치킨 집

# 모든 치킨 집중에서 m개의 치킨집을 찾는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0 
    # 모든 집에 대해서
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    
    return result

# 치킨 거리의 최솟값 출력하기

result = 1e9
for candidate in candidates:
    print(candidate)
    result = min(result, get_sum(candidate))

print(result)