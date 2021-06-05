
# 볼링 공의 개수 N, 공의 최대 무게 M
n, m = map(int, input().split())

# 볼링 공의 무게 K가 공백으로 구분되어 순서대로 입력
ball_array = list(map(int, input().split()))

ball_count = 0

for i in range(n-1):
    for j in range(i,n):
        if ball_array[i] != ball_array[j]: # 무게가 다른 공일때 카운트 증가
            ball_count += 1

print(ball_count)