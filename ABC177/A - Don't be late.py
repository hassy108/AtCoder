#https://atcoder.jp/contests/abc177/tasks/abc177_a

d, t, s = map(int, input().split())

if d > s*t:
    print('No')
else:
    print('Yes')