

# 2차원 리스트 시계방향 90도 회전
def turn_right(key):
    n = len(key)
    m = len(key[0])

    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    return result 

# 자물쇠 중간 부분이 모두 1ㄷ이닞 확인
def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2 ):
            if new_lock[i][j] != 1:
                return False
            return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 크기를 기존의 3배로 변환
    new_lock = [[0] * (n*3) for _ in range(n*3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = turn_right(key)
        for x in range(n * 2):
            for y in range(n * 2):
            # 자물쇠에 열쇠를 끼워 넣기
            for i in range(m):
                for j in range(m):
                    new_lock[x+i][y+j] += key[i][j]
            # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
            if check(new_lock) == True:
                return True
            for i in range(m):
                for j in range(m):
                    new_lock[x+i][y+j] -= key[i][j]

    return False


def solution(key, lock):
    answer = True
    return answer

# M*M 크기의 2차원 배열 key
m = int(input())
key = []

# N*N 크기의 2차원 배열 lock
n = int(input())
lock = []

for _ in range(m):
    input_key = list(map(int, input().split()))
    key.append(input_key)
    
for _ in range(n):
    input_lock = list(map(int, input().split()))
    lock.append(input_lock)
