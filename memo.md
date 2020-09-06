https://qiita.com/Hase-pro/items/16379a0c83f2725e3a11

___
### 20/06/11
## [ABC087B](https://qiita.com/watyanabe164/items/f6236b4c8bbd90def964)

# [インデントを気にしない入力](https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c)
`a, b, c, x = map(int, open(0).read().split())`  
入力後にctrl+C(EOFを入力する)

# [リスト内包表記](https://note.nkmk.me/python-list-comprehension/)  
`[式 for 変数名 in イテレータプルオブジェクト]`  
イテラプルオブジェクト(リストとか)の要素を式で評価，結果を新しいリストとして返す  
`s = [i**2 for i in range(5)]`  
0~4の2乗をsに代入

# [sum(list)](https://pycarnival.com/sum/)  
引数listの総和を返す

### [スライス](https://qiita.com/tanuk1647/items/276d2be36f5abb8ea52e)
シーケンス(リスト，文字列etc.)の一部を切り取ってコピーを返す．
`sequence[start:stop:step]`

___
### 20/08/11
# [セット](https://note.nkmk.me/python-set/)
セットは重複しない要素の集まり．集合演算を行える．  
`s = {1, 2, 2, 3, 4}`

___
### 20/09/02
# [辞書型](https://qiita.com/hz1_d/items/407dd13f90a8a4533d23)
キーバリュー方式のデータ構造
`d = {'x':2, 'y':3}`

___
### 20/09/05
# [累積和](https://qiita.com/drken/items/56a6b68edef8fc605821)
配列$A_{N-1}$について，配列$S_{N}$を以下のように定めたものを累積和という．
```math
A_{N-1}=\begin{Bmatrix}
    a_0 & a_1 & a_2 &...&a_{N-1}
\end{Bmatrix}
```
```math
S_N=\begin{Bmatrix}
    0 & a_0 & a_0+a_1 & a_0+a_1+a_2&...&a_0+a_1+a_2+...+a_{N-1}
\end{Bmatrix}
```
```math
S_N=\begin{Bmatrix}
    0 & s_1 & s_1+a_1 & s_2+a_2&...&s_{N-1}+a_{N-1}
\end{Bmatrix}
```
つまり1つ前までの要素を全て足したもの．

ここで，$A_n$から$A_m$までの和を求めるとき，累積和を用いると
```math
\sum_{i=n}^mA_i = \sum_{i=0}^mA_i-\sum_{i=0}^nA_i=s_m-s_n
```
で求められる(O(m-n)がO(1)で求められる)


[数式の書き方](https://shd101wyy.github.io/markdown-preview-enhanced/#/ja-jp/math)

___
### 20/09/06
# [for-else](https://python.civic-apps.com/else-loop/)
ループ内を`break`で抜けなかったとき`else`内が実行される
要素内で条件を満たさなかったとき，多重ループを抜けるときに使える．
```python
#要素内を探索して見つからない
for i in range(10)
    if i == 100:
        print('Found 100')
        break
else:
    print('Not found 100')
```
```python
#多重ループを抜ける
for i in range(10):
    for j in range(10):
        if i + j == 10:
            print('Found pair')
            break   #ここでbreakすると
    else:   
        print('Not Found pair')
        continue    #このcontinueが実行されず
    break   #このbreakが実行されてループを抜ける
```

# [Union-Find](https://pyteyon.hatenablog.com/entry/2019/03/11/200000)
無向グラフに対して
- 2つのグループをつなげる．
- 2つの要素が連結か調べる．
というクエリ(要求)を高速に行えるアルゴリズムとデータ構造．
リンク読め．

# [クラス](https://qiita.com/Usek/items/a206b8e49c02f756d636)
pythonでのクラスの書き方.
命名規則はCapWords方式(先頭大文字のラクダ)
ちなみに，変数と関数はヘビ
```python
class ClassName:
    #メンバ変数
    pub = 0     #普通に書くとpublic
    __pri = ''   #先頭に__(アンダーバー2つ)でprivate

    #コンストラクタ
    def __init__(self):     #selfはjavaのthis的なもの．必ず書く．
        self.pub = 2
        self.__pri = 'a'

    #メソッド
    def method(self, msg):
        print(msg)

#クラスの生成とメソッドの呼び出し
class_name = ClassName()
class_name.method('nya--')
```
