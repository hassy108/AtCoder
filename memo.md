https://qiita.com/Hase-pro/items/16379a0c83f2725e3a11

___
# 20/06/11
## [ABC087B](https://qiita.com/watyanabe164/items/f6236b4c8bbd90def964)

### [インデントを気にしない入力](https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c)
`a, b, c, x = map(int, open(0).read().split())`  
入力後にctrl+C(EOFを入力する)

### [リスト内包表記](https://note.nkmk.me/python-list-comprehension/)  
`[式 for 変数名 in イテレータプルオブジェクト]`  
イテラプルオブジェクト(リストとか)の要素を式で評価，結果を新しいリストとして返す  
`s = [i**2 for i in range(5)]`  
0~4の2乗をsに代入

### [sum(list)](https://pycarnival.com/sum/)  
引数listの総和を返す