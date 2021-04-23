"""
rule
 1. 숫자가 쓰인 카드들이 N*M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
 4. 따라서 처음에 카드를 골라낼 행을 선택할 때,
 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 새워야 한다.
"""
# n,m을 입력받기
"""
n,m = map(int, input().split())

min_line = 0
max = -1

# 행 선택
for i in range(n):
    data = list(map(int, input().split()))
    data.sort() # data 내림차순
    if data[0] > max:
        max = data[0] # 가장 큰 수와 비교하기

print(max)

"""
n, m = input(map(int, input().split()))
max = -1

for i in range(n):
    data = list(map(int, input().split))
    data.sort() # data 내림 차순
    if data[0] > max:
        max = data[0]

print(max)
