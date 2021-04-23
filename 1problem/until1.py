"""
    Rules
    1. N에서 1을 뺀다.
    2. N에서 K를 나눈다.
    3. N=1 이되는 1,2번의 최소 횟수를 구하려여라.
"""
"""
# n,k 입력받기
n, k = map(int,input().split())
count = 0

while n>1:
    if n % k == 0: # n이 k로 나누어질때
        n /= k
        count += 1
    elif n == 2: # n = 2 일때
        n -= 1
        count += 1
    else: # 나머지 경우
        result = int(n % k)
        n -= result
        count += result

print(count)
"""

# n,k 입력받기

n, k =  map(int, input().split())
count = 0

while n>1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1

print(count)