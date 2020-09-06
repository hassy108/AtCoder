#https://atcoder.jp/contests/abc177/tasks/abc177_d
'''
n, m =map(int,input().split())
l = [{int(x) for x in input().split()}]
ans = 0
for _ in range(m-1):
    a = {int(x) for x in input().split()}
    for j, s in enumerate(l):
        if s & a:
            l[j] |= a
            ans = max(ans, len(l[j]))
            if ans >= n:
                print(ans)
                exit()
            break
    else:
        l.append(a)
print(ans)
'''
'''
8行目以降の探索にO(n)，全体でO(nm)の時間計算量がかっている．
Union-Findを使うと探索にかかる時間を減らせる．O(log(n))
'''
class UnionFind:
    #par[x]でxの親のID，xが根ならその木のサイズに―をつけたもの
    def __init__(self, n):
        #全て根として初期化
        self.par = [-1] * n
    
    #xの根を返す
    def root(self, x):
        #xが根なら終了
        if self.par[x] < 0:
            return x
        #そうでないならxの親について調べる
        self.par[x] = self.root(self.par[x])    #xの根が親になるように更新
        return self.par[x]

    #xとyを結合
    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        #xとyが同じ根を持つ(＝同じ木に属する)なら終了
        if x == y:
            return
        #サイズの大きい木に小さい木を結合
        if self.par[x] > self.par[y]:   #xが大きくなるよう交換
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
    
    #xのサイズを返す
    def size(self, x):
        return -1 * self.par[self.root(x)]


#main
n, m = map(int, input().split())
uf = UnionFind(n)
#Union-FInd木を作る
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)      #1からではなく0からに
#サイズが最大のものを探す
ans = 0
for i in range(n):
    ans = max(ans, uf.size(i))
print(ans)

