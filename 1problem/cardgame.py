"""
rule
 1. 숫자가 쓰인 카드들이 N*M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
 4. 따라서 처음에 카드를 골라낼 행을 선택할 때,
 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 새워야 한다.
"""

# N,M를 공백으로 구분하여 입력 받기
n,m = map(int, input().split())

result = 0

for i in range(n): # N개의 행을 공백으로 구분하여 입력 받기
    data = list(map(int, input().split())) # N개의 행을 공백으로 구분하여 입력 받기
    """
    data.sort()
    if max < data[0]:
        max = data[0]
    """
    min_value = min(data)
    #'가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)




