"""
    - 입력조건
        - 첫 줄에 식량창고의 개수 N이 주어진다.(3<=N<=100)
        - 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다.( 0 <= K <= 1,000)
    - 출력조건
        - 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.
"""

n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = array[1]

for i in range(2, n):
    d[i] = max(int(d[i-2])+array[i], d[i-1])


print(d[n-1])
"""
# 정수 N을 입력 받기
n = int(input())
# 식량 정보 입력받기
array = list(map(int, input().split(' ')))


d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2,n):
    d[i] = int(d[i-2]) + array[i]
    d[i] = max(d[i-1], d[i])

print(d[n-1])
"""
