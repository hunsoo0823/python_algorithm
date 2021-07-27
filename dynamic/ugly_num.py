# n입력받기(n번째 못생긴 수)
n = int(input())

prime_array = [0] * n # 못생긴 수를 담기 위한 테이블(1차원 DP테이블)
prime_array[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
i2, i3, i5 = 0, 0, 0
# 처음 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수를 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    prime_array[l] = min(next2, next3, next5)

    if prime_array[l] == next2:
        i2 += 1
        next2 = prime_array[i2] * 2
    if prime_array[l] == next3:
        i3 += 1
        next3 = prime_array[i3] * 3
    if prime_array[l] == next5:
        i5 += 1
        next5 = prime_array[i5] * 5

print(prime_array[-1])
    