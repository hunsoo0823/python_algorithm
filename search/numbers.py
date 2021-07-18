from bisect import bisect_left, bisect_right

# N개의 원소, 정수 x
n, x = map(int, input().split())

# N개의 원소가 정수 형태로 공백으로 구분되어 입력
array = list(map(int, input().split()))

letf_side = bisect_left(array, x)
right_side = bisect_right(array, x)

result = abs(letf_side - right_side)

if result == 0:
    print(-1)
else:
    print(result)