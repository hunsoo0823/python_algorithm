
# M*M 크기의 2차원 배열 key
m = int(input())
key = []

# N*N 크기의 2차원 배열 lock
n = int(input())
lock = []

for _ in range(m):
    input_key = list(map(int, input().split()))
    key.append(input_key)
    

print(key)
