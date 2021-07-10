"""
 1. 입력이 빈 문자열일 경우 빈 문자열을 반환
 2. 문자열 w를 두 "균형잡힌 괄호 문자열", u, v 로 분리합니다.
    단, u는 "균형잡힌 괄호 문자열"로 더이상 분리할 수 없어야하며, v는 문자열이 될 수 있습니다.
 3. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    3-1, 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계 부터 다시 수행합니다.
 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    4-1, 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    4-2, 문자열 v에 대해 1단계로부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    4-3 ')'를 다시 붙입니다.
    4-4 u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    4-5 생성된 문자열을 반환합니다.
"""

def solution(input_str):
    left_count = 0
    right_count = 0
    v_check = 0

    u = '' # 임시로 저장할 문자열
    v = '' # 임시로 저장할 문자열

    answer = ''
    result = ''
    for str in input_str: 
        if v_check == 0:
            if str == '(':
                left_count += 1
                u += str
                if left_count == right_count: # 균형잡힌 괄호 문자열이나 올바른 괄호 문자열이 아닌 경우
                    v_check = 1 # 나머지는 v문자열에 저장
            elif str == ')':
                right_count += 1
                u += str
                if left_count == right_count: # 올바른 괄호 문자열일 경우
                    answer += u
                    u = ''
                    left_count, right_count = 0, 0    
        elif v_check == 1:
            v += str

    if v_check == 1:
        result += '('
        result += solution(v) # 4-2 수행
        result += ')' # 4-3 수행

        answer += result
    
        u = list(u[1:-1]) # 첫번째 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
    
        answer += "".join(u)
        return answer

    elif v_check == 0:
        return answer


input_str = input()
sol = solution(input_str)
print(sol)

    