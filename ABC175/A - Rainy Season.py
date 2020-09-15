
s = input()
c = 0
a = 0
for i in s:
    if i == 'R':
        c += 1
        a = c
    else:
        c = 0
print(a)