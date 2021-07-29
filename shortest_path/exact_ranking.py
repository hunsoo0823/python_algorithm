# 학생수 n, 두 학생의 성적을 비교한 횟수 m
n, m = map(int, input().split())

INF = 1e9
# 결과를 저장할 변수
result = 0

# 리스트 거리 초기화
array_grade = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 거리 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            array_grade[i][j] = 0

# 두 학생의 성적을 비교한 결과 나타내는 두양의 정수 A,B
for _ in range(m):
    a, b = map(int , input().split())
    array_grade[a][b] = 1

# 플루이드 워셜 알고리즘
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            array_grade[a][b] = min(array_grade[a][b], array_grade[a][k]+array_grade[k][b])

# a->b 혹은 b->a로 가는 방법이 있는지 확인해서 가능하면 count+1
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if array_grade[i][j] != INF or array_grade[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)

for i in range(1, n+1):
    for j in range(1, n+1):
        if array_grade[i][j] == INF:
            print('%3s' % 'INF', end=' ')
        else:
            print('%3d' % array_grade[i][j], end=' ')
    print()


