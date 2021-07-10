from collections import deque

q = deque()

q.append((1,2,3))
a, b, c = q.popleft()

print(a,b,c)