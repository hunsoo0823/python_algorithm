
# N명의 모험가 입력
n = int(input())

# 각 모험가의 공포도 측정
fear_array = list(map(int,input().split()))

# 공포도 오른차순 정렬
fear_array.sort()

# 그룹 수 변수
guild_group = 0
# 그룹안의 인원수 체크
count = 0

for fear in fear_array: # 현재 그룹에 포함된 인원
    count += 1 # 그룹에 포함시키기
    if count >= fear: # 공포도보다 그룹의 인원수가 많다면 출격
        guild_group += 1 # 그룹 수 증가
        count = 0 # 새로운 그룹을 위한 초기화

print(guild_group)



