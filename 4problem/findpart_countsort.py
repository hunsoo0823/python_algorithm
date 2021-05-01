"""
    findpart.py의 계수 정렬 버전
"""

n = int(input())

shop = [0] * 1000001

for i in input().split():
    shop[int(i)] = 1

m = int(input())
cus = list(map(int, input().split()))

for i in cus:
    if shop[i] == 1:
        print('yes', end=' ')
    else:
        print('no',end=' ')

