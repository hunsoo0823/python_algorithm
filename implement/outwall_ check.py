# 외벽의 길이 n (1<=n<=200)
# 취약지점의 위치가 담긴 배열 week(1<=week<=15)
# 각 친구가 이동할 수 있는 거리가 담긴 배열 dist(1<=len(dist)<=8, 1<=element(dist)<=100)

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1
    for start in range(length):
        for friends in dist(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start+length):
                # 점거할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구들 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
            return -1
    return answer    

    

