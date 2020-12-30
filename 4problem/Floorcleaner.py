"""
 - 입력조건
    - 첫째 줄에 N이 주어진다. ( 1<=N<=1,000)
    - 첫쨰 절에 2 x N 크기의 바닥을 채우는 방법의 수를 796, 796으로 나눈 나머지를 출력한다.
"""

n = int(input())

array = [0] * 1001

array[1] = 1
array[2] = 3

for i in range(3, n+1):
    array[i] = array[i-2] * 2 + array[i-1]

print(array[n])

"""
# 정수 N을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
array = [0] * 1001

array[1] = 1
array[2] = 3

# 다이나믹 프로그래밍(Dynamic Programming) 진행
for i in range(3,n+1):
    array[i] = array[i-1] + array[i-2] * 2

print(array[n])
"""