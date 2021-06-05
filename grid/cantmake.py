
# 동전의 개수 n
n = int(input())

# 화폐의 단위를 나타태는 N개의 자연수
coin_array = list(map(int,input().split()))
coin_array.sort()

target = 1
for coin in coin_array:
    if target < coin:
        break
    target += coin

print(target)