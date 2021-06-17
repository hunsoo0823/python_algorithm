
# 첫째줄 문자열 S입력

str = input()
n = len(str)

str_alpha = []
num = 0

for i in range(n):
    if(str[i].isalpha()):
        str_alpha.append(str[i])
    else:
        num += int(str[i])

str_alpha.sort()

for str in str_alpha:
    print(str, end='')
print(num)