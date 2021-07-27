# 문자열 A입력
before_str = input()

# 문자열 B입력
after_str = input()
count = 0

if len(before_str) <= len(after_str): # 뒤에 문자가 더 클 경우,
    count = len(after_str) - len(before_str) # insert
    for str in before_str: # 일치하지 않은 문자열만큼 replace
        if str in after_str: # 일치하는 문자
            after_str = after_str.replace(str, "")
        else: # 일치하지 않은 경우
            count += 1

else: # 앞의 문자열이 더 클 경우
    count = len(before_str) - len(after_str) # delete
    for str in after_str: # 일치하지 않은 문자열 만큼 replace
        if str in before_str:
            before_str = before_str.replace(str,"")
        else:
            count += 1 

print(count)