"""
  - 입력조건
    - 첫번째 줄에 두정수 N,M(4<=N, M<=200)이 주어집니다.
    다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
    각각의 수들은 공백없이 붙어서 입력으로 제시된다. 또한 시작칸과 마지막칸은 항상 0이다.
  - 출력조건
    첫째 줄에 최소 이동 칸의 개수를 출력한다.
"""

n, m = map(int,input().split())

mapping = []
for i in range(n):
    mapping.append(list(map(int,input())))

def escape(x,y,bx,by):

    if x<0 or x>=n or y<0 or y>=m:
        return False

    if mapping[x][y] == 1:
        if x > 0 or y > 0:
            mapping[x][y] = mapping[bx][by] + 1
        if x == n - 1 and y == m - 1:
            return True
        escape(x+1,y,x,y)
        escape(x,y+1,x,y)
        escape(x-1,y,x,y)
        escape(x,y-1,x,y)
    else:
        return False

escape(0,0,0,0)
print(mapping[n-1][m-1])


