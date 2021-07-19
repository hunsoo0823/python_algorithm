# 수열 N
n = int(input())

# 배열 요소 입력 받기
array = list(map(int, input().split()))

def binary_search(array, start, end):
    
    if start > end:
        return None

    mid = start + end

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)

result = binary_search(array, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)