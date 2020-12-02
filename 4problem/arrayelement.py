"""
 - 입력조건
    첫번째 줄에 N,K가 공백으로 구분되어 입력된다.(1<=N<=100,000, 0<=K<=N)
    두번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
    세번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수입니다.

 - 출력조건
    최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최갯값을 출력한다.
"""

n,k = map(int, input().split()) # N과 K를 입력받기

a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() # 내림차순
b.sort(reverse=True) #₩오름차순






for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

