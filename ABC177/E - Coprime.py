#https://atcoder.jp/contests/abc177/tasks/abc177_e

'''
pairwiseは愚直にやるとO(n^2)で詰み．

Aに同じ素因数を持つ数が2回以上出てくればpairwiseではない．

解1. https://youtu.be/D6dr2CrEgns?t=3323
2~10^6 がAに何回出てくるかカウントし，
2,4,6,8,..., 3,6,9,12,...の和が2を超えるかチェック．
O(AlogA)

解2. https://atcoder.jp/contests/abc177/editorial/82
Aiを素因数分解し同じ素因数を持つかチェック．
O(AloglogA)
'''
import math

#main
MAX_A = 10**6+5     #Aの最大値10^6
n = int(input())
a = [int(x) for x in input().split()]
#各数が出てくる回数を保存
b = [0] * MAX_A
for i in range(n):
    b[a[i]] += 1

#pairwise判定
f = False
for i in range(2, MAX_A):   #0,1は除く
    c = 0
    #i=2ならj=2,4,6,8,...のようにiを因数に持つ数が何個あるかカウント
    for j in range(i, MAX_A, i):
        c += b[j]
        if c > 1:
            f = True
            break
    if f:
        break
    else:
        print('pairwise coprime')
        exit()

#setwise判定
g = 0
for ai in a:
    g = math.gcd(g, ai)
if g == 1:
    print('setwise coprime')
    exit()

#どちらでもない
print('not coprime')


