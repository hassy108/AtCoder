#https://atcoder.jp/contests/abc176/tasks/abc176_e

import numpy as np

h, w, m = map(int, input().split())
a = np.zeros((h, w))
for _ in range(m):
    hi, wi = map(lambda x:int(x)-1, input().split())
    a[hi][wi] += 1
#->向きの合計
sum_xs = np.sum(a, axis = 1)
max_x = np.max(sum_xs)
index_x = np.argmax(sum_xs)
#↓向きの合計
sum_ys = np.sum(a, axis = 0)
max_y = np.max(sum_ys)
index_y = np.argmax(sum_ys)

print(int(max_x + max_y - a[index_x][index_y]))