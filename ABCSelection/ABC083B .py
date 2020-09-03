#https://atcoder.jp/contests/abs/tasks/abc083_b

n, a, b = map(int, input().split())

sum = 0
for i in range(a, n+1):
    j = i
    x = 0
    while(j > 0):
        x += j % 10 
        j //= 10
    if a <= x <= b:
        sum += i
print("%d" %(sum)) 

"""
https://gist.github.com/yumechi/c13c7033995daf401dc554abb3c4dc72
文字列はイテレータプルだからsum()が使える
各桁の合計を求める部分を sum([int(j) for j in str(i)] とする
7~13
if a <= sum([int(j) for j in str(i)] <= b)
"""
