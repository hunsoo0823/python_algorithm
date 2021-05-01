"""
 - 입력 조건
    -  첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. ( 1<=N<=1,000,000, 1<=M<=2,000,000)
    -  둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 덕을 사갈수 있다.
    높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
 - 출력 조건
    - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
"""

n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in rice_cake:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

