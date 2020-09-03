#https://atcoder.jp/contests/abs/tasks/abc087_b

a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
for i in range(0, a+1):
    for j in range(0, b+1):
        for k in range(0, c+1):
            if i*500 + j*100 + k*50 == x:
                cnt += 1
print("%d" %(cnt))


#https://qiita.com/watyanabe164/items/f6236b4c8bbd90def964


