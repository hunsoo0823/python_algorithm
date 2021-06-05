def solution(food_times, k):
    answer = 0
    i = 0 # 초를 세기 위한 변수

    while True:
        if food_times[answer] != 0: # 먹을 수 있는 음식이 있는 경우
            if i >= k: # i==k가 되는 순간 멈춤
                break
            food_times[answer] -= 1 # 음식 소모
            i += 1 # 시간 증가

        answer += 1 # 다음에 먹어야 하는 음식 번호
        if answer == n: # 범위를 벗어난 경우 원래 번호로 초기화
            answer = 0

    return answer

# 먹어야할 n개의 음식, k초의 방송이 중단된 시간
n, k = map(int, input().split())

# 각 음식 섭취에 필요한 시간
food_time = list(map(int, input().split()))

result = solution(food_time, k)

print(result+1)