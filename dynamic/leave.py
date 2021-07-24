# 퇴사전 남은 기간 n일
n = int(input())

array = []
# 상담시간 T, 금액 P
for i in range(n):
    array.append(list(map(int, input().split())))

# array = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
expensive = [0 for _ in range(n)]

for i in range(n):
    
    index = i + array[i][0]-1
    if index < n:
        expensive[index] = max(expensive[index], (array[i][1] + expensive[i-1]))

max_num = max(expensive)
print(max_num)