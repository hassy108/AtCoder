#https://atcoder.jp/contests/abs/tasks/arc089_a

N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

old = {'t':0, 'x':0, 'y':0}
for i in range(N):
    if t[i]-old['t'] < abs(x[i]-old['x']) + abs(y[i]-old['y']) or t[i]%2 != (x[i]+y[i])%2:
        print('No')
        exit()
    old = {'t':t[i], 'x':x[i], 'y':y[i]}
print('Yes')

"""
https://qiita.com/Kyan_TK/items/65251777d63e00448a70
今いる地点から目標地点までの距離を考える必要がある．
t[i] < x[i]+y[i] は(0,0)から(x[i],y[i])の距離しか考慮してない．
"""
