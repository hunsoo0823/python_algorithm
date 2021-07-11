
def solution(n, build_frame):
    answer = [[]]

    # 맵 생성 2인경우 아무것도 없는 빈공간을 의미
    map = [[[2] * n] * 2 for _ in range(n) for _ in range(2)]

    for frame in build_frame:

        x = frame[0]
        y = frame[1]

        if frame[3] == 0: # 기둥
            if frame[4] == 1: # 기둥 설치
                if y == 0: # 바닥인 경우
                    map[n-y][x][0] = 0 # 맵 갱신
                    answer.append([x, y, 0])
                elif map[n-y+1][x][0] == 0: # 기둥 위인 경우 체크
                    map[n-y][x][0] = 0 # 맵 갱신
                    answer.append([x, y, 0]) 
                elif map[n-y+1][x][1] == 1: # 보 위인 경우 체크
                    map[n-y][x][0] = 0 # 맵 갱신
                    answer.append([x, y, 0])
                else: # 새울 수 없다고 판단
                    continue
            if frame[4] == 0: # 기둥 철거
                if map[n-y-1][x][0] == 0: # 위에 기둥이 있는 경우 철거 불가
                    continue
                elif map[n-y][x][1] == 1:  # 기둥기준 오른쪽에 보가 있는 경우
                    if x-1 < 0 or map[n-y][x-1][1] != 1: # 맨왼쪽인 경우, 왼쪽에 기둥이 없는 경우 철거 불가
                        continue
                elif map[n-y][x-1][1] == 1: # 기둥 기준 왼쪽에 보가 있는 경우 , 위의 경우에서 왼쪽에 보가 없다는 것을 확인했기 때문에 철거 불가
                    continue
                else: # 그외의 경우 : 철거 가능
                    map[n-y][x][0] = 2
                    answer.remove([x, y, 0])

        if frame[3] == 1: # 보  
            if frame[4] == 1: # 보 설치
                if y == 0: # 바닥인 경우
                    continue # 설치 불가
                elif x < n and (map[n-y][x][0] == 0 or map[n-y][x+1][0]) == 0 : # 기둥이 존재하는 경우 
                    map[n-y][x][1] = 1
                    answer.append([x, y, 1])
                if map[n-y][x-1][1] == 1 and map[n-y][x+1][1] == 1: # 설치하려는 장소에 양옆에 다른 보가 동시에 연결이 되는 경우
                    map[n-y][x][1] = 1
                    answer.append([x, y, 1])
            if frame[4] == 0: # 보 철거
                if map[n-y][x-1][1] == 1: # 왼쪽에 보가 있는 경우
                    if map[n-y][x][0] == 0: # 왼쪽에 보가 있는데 밑에 기둥이 연결된 경우
                        answer.remove([x, y, 1])
                        map[n-y][x][1] = 2
                    else: # 기둥이 존재하지않기에 철거 불가
                        continue
                if map[n-y][x+1][1] == 1: # 오른쪽에 보가 있는 경우
                    if map[n-y][x+1][]
                    


    
    return answer
