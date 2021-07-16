# 집의 갯수 n
n = int(input())

# n채의 집의 위치가 공백을 구분하여 입력
antena = list(map(int, input().split()))

antena.sort()

mid = antena[(n-1)//2]
print(mid)
