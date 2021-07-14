board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]

# 동, 서, 남, 북 이동
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]

# 반시계 방향 4회전
tx = [1, -1, -1, 1]
ty = [1, 1, -1, -1]


def solution(board):
    answer = 1e9
    
    count = 0
    lx, ly = 0, 0
    rx, ry = 0, 1 

    answer = min(answer, bfs(lx, ly, rx, ry, count, board))
    return answer

def bfs(lx, ly, rx, ry, count, board):
    # 상하좌우 움직이기
    for i in range(4):
        nlx = lx + mx[i]
        nly = ly + my[i]
        nrx = rx + mx[i]
        nry = ry + my[i]

        # 범위 밖을 벗어나지 않는 경우
        if 0 <= nlx < len(board[0]) and 0 <= nly < len(board[0]) and 0 <= nrx < len(board[0]) and 0 <= nry < len(board[0]):
            # 움직이려는 곳에 벽이 없는 경우
            if board[nlx][nly] != 1 and board[nrx][nry] != 1:
                # 도착한 경우
                if (nlx == len(board) and nly == len(board)) or (nrx == len(board) and nry == len(board)):
                    return count
                count += 1
                # print("i, lx, ly, rx, ry, count : {}, {}, {}, {}, {}, {} ".format(i, nlx, nly, nrx, nry, count))
                bfs(nlx, nly, nrx, nry, count, board)
                count -= 1

    # 반시계 방향으로 회전
    for i in range(4):
        nlx = lx + tx[i]
        nly = ly + ty[i]

        # 회전시 벽에 부딪히는 조건
        clx = lx + mx[i] 
        cly = ly + my[i]

        if 0 <= nlx < len(board[0]) and 0 <= nly < len(board[0]):
            if board[clx][cly] != 1:
                if board[nlx][nly] != 1:
                    # 목적지에 도착한 경우
                    if (nlx == len(board) and nly == len(board)) or (nrx == len(board) and nry == len(board)):
                        return count
                    count += 1
                    bfs(nlx, nly, nrx, nry, count, board)
                    count -= 1

output = solution(board)
print(output)           




                



