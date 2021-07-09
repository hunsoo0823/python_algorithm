from itertools import permutations

# 수의 갯수 n (2<=n<=11)
n = int(input())

number = []
# A1,A2,...An 
input_num = list(map(int, input().split()))
for n in input_num:
    number.append(n)

# 합이 n-1인 연산자의 갯수(+,-,*,/)
input_operator = list(map(int, input().split()))
operator = []

for i in range(n):
    if i == 0:
        for i in range(input_operator[i]):
            operator.append('+') # 덧셈
    elif i == 1:
        for i in range(input_operator[i]):
            operator.append('-') # 뺄셈
    elif i == 2:
        for i in range(input_operator[i]):
            operator.append('*') # 나눗셈
    elif i == 3:
        for i in range(input_operator[i]):
            operator.append('//') # 곱셈

operator_per = list(permutations(operator, len(operator))) # 연산자들의 모든 조합을 구하기

max_result = -1e9
min_result = 1e9

for per in operator_per:
    result = number[0]
    per = list(per)
    
    for i in range(1, len(number)):
        op = per.pop()
        if op == '+':
            result += number[i]
        elif op == '-':
            result -= number[i]
        elif op == '*':
            result *= number[i]
        elif op =='//':
            result = int(result / number[i]) # c++14 기준 나눗셈
        
    
    max_result = max(result, max_result)
    min_result = min(result, min_result)

print(max_result)
print(min_result)    
    
    



