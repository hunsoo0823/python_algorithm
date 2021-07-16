# 카드 묶음의 갯수
n = int(input())

# n개 줄에 카드 묶음 입력받기
card = []
for _ in range(n):
    card_input = int(input())
    card.append(card_input)

card.sort()

result = 0
temp = card[0]

for i in range(1,n):
    temp += card[i]
    result += temp

print(result)