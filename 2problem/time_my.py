"""
 첫번째 줄에 정수 N이 입력된다.(0<=N<=23)
 00시00분00초 부터 N이 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""

#시간 입력 받기
n = int(input())

hour,min,sec = 0, 0 ,0
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
