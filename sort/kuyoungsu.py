# 반 학생수 입력
n = int(input())

# n명 학생의 정보를 입력 받음
students = []
for _ in range(n):
    input_data = input().split()
    # 이름은 문자열, 각 과목점수는 정수향으로 변환하여 저장
    students.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])

                                                                           