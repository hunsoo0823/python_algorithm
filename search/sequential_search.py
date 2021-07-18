# 순차 탐색 소스코드 구현
def sequetial_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 #  현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
    
print("생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하시오.")
input_data = input().split()

n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수 만큼 문자열을 입력하시오. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행결과 출력
print(sequetial_search(n, target, array))