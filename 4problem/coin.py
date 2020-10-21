"""
    - 입력조건
        - 첫째 줄에 N,M이 주어진다.(1<=N<=100, 1<=M<=10,000)
        - 이후에 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수 이다.
    - 출력조건
        - 첫째 줄에 경우 x를 출력한다.
        - 불가능 할때는 -1을 출력한다.
"""

# 정수 N,M을 입력받기
n, m = map(int, input().split())

# N개의 화페 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산 저장하기 위한 DP 테이블 초기화
coin = [10001] * (m+1)

# 다이나믹 프로그래밍
for i in array:
    coin[i] = 1

for i in range(array[n-1]+1, m+1):
    for j in array:
        if coin[i - j] != 10001:
            coin[i] = min(coin[i], coin[i-j]+1)

# 결과 출력
if coin[m] == 10001:
    print(-1)
else:
    print(coin[m])
