"""
    - 입력조건
        - 첫째 줄에 N,M이 주어진다.(1<=N<=100, 1<=M<=10,000)
        - 이후에 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수 이다.
    - 출력조건
        - 첫째 줄에 경우 x를 출력한다.
        - 불가능 할때는 -1을 출력한다.
"""

# 동전의 갯수 n, 금액 m
n, m = map(int, input().split())

# 동전 입력
coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(len(coin)):
    for j in range(coin[i] ,m+1):
        if d[j - coin[i]] != 10001:
            d[j] = min(d[j] , d[j-coin[i]]+1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)


