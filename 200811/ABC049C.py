#https://atcoder.jp/contests/abs/tasks/arc065_a

s = input()
l = ['eraser', 'erase', 'dreamer', 'dream']

for i in l:
    s = s.replace(i, '')
if s:
    print('NO')
else:
    print('YES')
