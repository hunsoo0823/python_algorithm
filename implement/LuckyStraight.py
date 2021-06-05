lucky = input()
n = len(lucky)
left, right = 0, 0

for i in range((n//2)):
    left += int(lucky[i])

for i in range((n//2), n):
    right += int(lucky[i])

if left == right:
    print("LUCKY")
else:
    print("READY")