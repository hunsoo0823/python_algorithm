"""
    입력 조건
    - 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
    - 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하 이다.
    - 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
    - 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하 이다.
    출력조건
    - 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다.
"""

# 이진 탐색 소스코드 구현(재귀)
def binarysearch(array, target, start, end):
    if start > end:
        return False

    mid = (start+end)//2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarysearch(array, target, start, mid-1)
    else:
        return binarysearch(array, target, mid+1, end)

   
array_shop = []
# 상점의 n개의 부품 번호  
n = int(input())
array_shop = list(map(int, input().split()))
array_shop.sort()

# 손님의 m개의 부품 번호
array_cus = []
m = int(input())
array_cus = list(map(int, input().split()))
array_cus.sort()


for i in array_cus:
    result = binarysearch(array_shop, i, 0, n-1) # 이진탐색으로 찾기
    
    if result == True:
        print('yes', end=' ')
    else:
        print('no', end=' ')
            