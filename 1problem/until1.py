"""
    Rules
    1. N에서 1을 뺀다.
    2. N에서 K를 나눈다.
    3. N=1 이되는 1,2번의 최소 횟수를 구하려여라.
"""

n,k = map(int, input().split())
count = 0

while n >= k :
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1

while n != 1:
    n -= 1
    count += 1

print(count)

