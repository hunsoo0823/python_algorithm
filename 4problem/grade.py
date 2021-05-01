"""
 - 입력조건
    첫 번째 줄에 학생의 수 N이 입력된다.(1<=N<=100,000)
    두 번째 줄로부터 N+1번째 줄에는 학생의 이름을 나타내는 문잘열A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
    문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.
 - 출력조건
    모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
"""

n = int(input())

grade_array = []
for i in range(n):
    input_data = input().split()

    grade_array.append((input_data[0], int(input_data[1])))

grade_array = sorted(grade_array, key = lambda studnet : studnet[1])

for student in grade_array:
    print(student[0], end=' ')


