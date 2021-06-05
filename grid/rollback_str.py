# 문자열 입력받기
array = list(map(int, input()))

# 전 문자 확인하기
count = [0, 0]

for i in range(1, len(array)):
    prev = array[i-1]
    now = array[i]

    # 숫자가 바뀌면 전 숫자를 +1
    if prev != now:
           count[prev] += 1

    # 끝날때를 체크
    if i == (len(array)-1):
        count[now] += 1

if count[1] > count[0]:
    print(count[0])
else:
    print(count[1])
