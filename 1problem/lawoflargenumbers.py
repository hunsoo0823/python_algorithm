"""
다양한 수로 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속적으로해서 K번을 초과해서 더해줄 수 없는 것이 법칙의 특징이다.

입력 조건 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때, 큰수의 법칙에 따른 결과를 출력
( 2<=N<1,000 , 1<=M<=10,000, 1<=K<=10,000) 각 자연수는 공백으로 구분, K <= M
"""

# N,M,K를 공백으로 구분하여 입력 받기
n,m,k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수
result = 0
temp = k # k의 횟수를 세줄 임시 변
um = m

# 1
while True:
    if um == 0: # m이 0이면 반복문 탈출
        break
    else:
        result += first # 가장 큰 수 k 더하기
        um -= 1
        temp -= 1
        if temp == 0: # k번 더하고 , m이 0이 아닌경
            if um != 0:
                result += second # 두번째 큰 수를 더하
                um -= 1
                temp = k # 임수 변수 초기화
print(result)

um = m
result = 0

# 2
while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if um == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        um -= 1 # 더할 때 마다 1씩 뺴기
    if um == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한번 더하기
    um -= 1 # 더할 때마다 1씩 빼기

print(result)

# 3
um = m
result = 0

count = int(um/(k+1)) * k + m % (k+1) # 가장 큰 수가 더해지는 횟수 계
result += count * first
result += (um-count) * second

print(result)







