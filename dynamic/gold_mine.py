# 첫쨰줄 테스트 케이스 T
t = int(input())

# 금광 이동
dx = [-1,0,1]
dy = [1,1,1]

for _ in range(t):

    # nxm 금광
    n, m = map(int, input().split())

    # 금광의 금의 갯수 입력받음(n*m개)
    input_gold = list(map(int, input().split()))
    array = []

    temp_array = []
    count = 0
    for gold in input_gold:
        count += 1
        temp_array.append(gold)

        if count % m == 0:
            array.append(temp_array)
            temp_array = []

    gold_mine = [[0] * m for _ in range(n)]

    for i in range(n):
        gold_mine[i][0] = array[i][0]

    for y in range(m-1):
        for x in range(n):
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n:
                    continue
                else:
                    gold_mine[nx][ny] = max(gold_mine[nx][ny], gold_mine[x][y] + array[nx][ny])
            
    max_num = -1
    for i in range(n):
        if gold_mine[i][m-1] > max_num:
            max_num = gold_mine[i][m-1]

    print(max_num)


