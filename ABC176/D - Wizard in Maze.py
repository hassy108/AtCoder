#https://atcoder.jp/contests/abc176/tasks/abc176_d

"""
コストが0または1の無向グラフと見ると，01-BFSが使える．
https://betrue12.hateblo.jp/entry/2018/12/08/000020
コスト0の移動を試し，コスト1の移動を試す
それまでの総コストが小さいなら更新
キューにコストを入れることで，同じ地点がコスト0，1それぞれでキューに追加されることを防ぐ
"""
from collections import deque

h, w = map(int, input().split())
ch, cw = map(lambda x:int(x)-1, input().split())    #0indexにして受け取る
dh, dw = map(lambda x:int(x)-1, input().split())
s = [input() for _ in range(h)]
#距離(スタートからijまでの総コスト)
MAX_DIST = 10**9
dist = [[MAX_DIST]*w for _ in range(h)]
dist[ch][cw] = 0
#両端キュー
dq = deque()
dq.append((ch, cw, dist[ch][cw]))
#上下左右移動
mx = [-1,+1, 0, 0]
my = [ 0, 0,-1,+1]

#01-BFS
while dq:
    i, j, d = dq.popleft()
    #コスト0で追加されたキューが，コスト1として追加されたとき評価しない
    if d > dist[i][j]:
        continue
    #歩いて移動
    d = dist[i][j]
    for n in range(4):
        i2 = i + mx[n]
        j2 = j + my[n]
        #範囲外へは進めない
        if not (0 <= i2 < h and 0 <= j2 < w):
            continue
        #壁へは進めない
        if s[i2][j2] == '#':
            continue
        #距離が小さければ更新
        if d < dist[i2][j2]:
            dist[i2][j2] = d
            #キューの先頭に追加
            dq.appendleft((i2,j2,dist[i2][j2]))

    #ワープ移動
    d += 1
    eju = -2
    for ei in range(-2,3):
        i2 = i+ei
        #範囲外へは進めない
        if i2 < 0:
            continue
        if h <= i2:
            break
        for ej in range(eju,3):
            j2 = j+ej
            #範囲外へは進めない
            if j2 < 0:
                eju = ej+1
                continue
            if w <= j2:
                break
            #壁へは進めない
            if s[i2][j2] == '#':
                continue
            #距離が小さければ更新
            if d < dist[i2][j2]:
                dist[i2][j2] = d
                #キューの末尾に追加
                dq.append((i2, j2,dist[i2][j2]))

if MAX_DIST == dist[dh][dw] :
    print(-1)
else:
    print(dist[dh][dw])
