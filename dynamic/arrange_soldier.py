# n입력 받기
n = int(input())

#soldier = []
#soldier.append(list(map(int, input().split())))
soldier = [15,11,4,8,5,2,4]

# 전투력 최대값을 계산할 배열
result_power = [0 for _ in range(n)]
result_num = [1 for _ in range(n)]
# 첫번쨰 값 초기화(병사가 한명이라고하면 나올수 있는 값은 무조건 하나)
result_power[0] = soldier[0] 

for i in range(1,n):
    # 앞쪽에 있는 병사가 뒤쪽에 있는 병사 보다 전투력이 높을때,
    if soldier[i] < soldier[i-1]:
        result_power[i] = result_power[i-1] + soldier[i]
        result_num[i] = result_num[i-1] + 1
    # 앞쪽에 있는 병사가 뒤쪽에 있는 병사 보다 전투력이 같거나 작을때,
    else:
        # 앞으로 이동하면서 인덱스 기준 전투력이 높은 병사를 찾음
        for j in range(i-2,0,-1):
            if soldier[j] > soldier[i]:
                result_power[i] = result_power[j] + soldier[i]
                result_num[i] = result_num[j] + 1
                break
            # j = 0 일때 앞에 전투력이 높은 병사가 없음
            if j == 0:
                result_power[j] = soldier[j]

# 제외해야할 최대 수
max_execption = n - result_num[result_power.index(max(result_power))]
print(max_execption)