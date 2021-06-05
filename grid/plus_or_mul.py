
# 문자열 S입력 받기

num_array = list(map(int, input()))

check_first = False # 첫번째 문자열 체크
result = 0

for num in num_array:
    if check_first == False and num != 0: # 첫번째 문자열은 무조건 더해야함 대신, 0일때는 첫번째 문자열이 아닌것으로 간주
        result += num
        check_first = True # 첫번째 문자열 확인
    else:
        if num == 0 or num == 1:# 0,1인경우 더하기
            result += num
        else: # 그 외인 경우는 모두 곱하기
            result *= num

print(result)