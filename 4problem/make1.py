"""
 - 입력조
  - 첫번째 줄에 정수 X가 주어진다(1<=X<=30,000)
  - 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""

# 정수 x 입력 받기
x = int(input())

# 배열 생성
d = [0] * 30001

for i in range(2, x+1):

    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
