#https://atcoder.jp/contests/abs/tasks/abc088_b

n =int(input())
a = sorted( [int(x) for x in input().split()], reverse = True )

diff = 0;
for i in range(0,n):
    if 0 == i % 2:
        diff += a[i]
    else:
        diff -= a[i]
print("%d" %(diff))

"""
https://note.com/keisuke_funabiki/n/nec9df628f77c#wJfok
スライスを使うことで奇数偶数を簡単に分けられる．
print( sum(a[::2]) - sum(a[1::2]) )

"""