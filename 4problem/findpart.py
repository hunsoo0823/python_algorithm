"""
    입력 조건
    - 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
    - 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하 이다.
    - 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
    - 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하 이다.
    출력조건
    - 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다.
"""

def binary_search(start, end, target, array):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())

shop = list(map(int, input().split()))
shop.sort()

m = int(input())
cus = list(map(int, input().split()))

for i in range(m):
    result = binary_search(0, n, cus[i], shop)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

