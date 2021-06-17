def solution(s):

    n = len(s)
    str_min = 10001
    answer = 0
    count = 1

    for i in range(1, n+1):
        result = []
        for j in range(0, n, i):
            if s[j:j+i] != s[j+i:j+(2*i)]:
                if count == 1:
                    result.append(s[j:j+i])
                else:
                    str_count = str(count)
                    result.append(str_count)
                    result.append(s[j:j+i])
                    count = 1
            else:
                count += 1
        str_fin=len(''.join(result))
        if str_min > str_fin:
            answer = i
            str_min = str_fin
    return answer

str_origin = input()

sol = solution(str_origin)

print('문자열을 {}개 단위로 압축했을 때 가장 짧습니다.'.format(sol))