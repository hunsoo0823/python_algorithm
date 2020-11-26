"""
다양한 수로 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속적으로해서 K번을 초과해서 더해줄 수 없는 것이 법칙의 특징이다.

입력 조건 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때, 큰수의 법칙에 따른 결과를 출력
( 2<=N<1,000 , 1<=M<=10,000, 1<=K<=10,000) 각 자연수는 공백으로 구분, K <= M
"""

# n,m,k 의 값 입력받기
n,m,k = map(int, input().split())

# 입력 array
input_ary=list(map(int, input().split()))
input_ary.sort(reverse=True)

first_big = input_ary[0]
second_big = input_ary[1]

result = (m // (k+1)) * (first_big*k + second_big) + (first_big * m%(k+1)) # 결과 계산
print(result)
