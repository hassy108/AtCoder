#https://atcoder.jp/contests/abs/tasks/abc085_b

n = int(input())
s = []
b = 0
for i in range(n):
    a = int(input())
    if a not in s: 
        b += 1
    s.append(a)
print(b)

"""
http://delta114514.hatenablog.jp/entry/2018/03/15/014555#7%E5%95%8F%E7%9B%AE-ABC085B---Kagami-Mochi
セット(順序なし集合)を使えば判定しなくてよい
"""
