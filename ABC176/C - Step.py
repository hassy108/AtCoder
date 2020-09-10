#https://atcoder.jp/contests/abc176/tasks/abc176_c

n =  int(input())
a = [int(x) for x in input().split()]
c = 0
for i in range(n-1):
    if a[i] > a[i+1]:
        c += a[i] - a[i+1]
        a[i+1] = a[i]
print(c)