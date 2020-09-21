"""
 첫번째 줄에 정수 N이 입력된다.(0<=N<=23)
 00시00분00초 부터 N이 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""

#시간 입력 받
n = int(input())

hour, sec, min = 0, 0, 0
count = 0

while hour <= n:
    sec += 1
    if sec > 59:
        sec = 0
        min += 1
        if min > 59:
            min = 0
            hour += 1

    #시간에 3이 들어가있는지 확인
    if str(sec).find('3') != -1 or str(min).find('3') != -1 or str(hour).find('3') != -1:
        count += 1

print(count)

