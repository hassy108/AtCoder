#https://atcoder.jp/contests/abs/tasks/abc085_c

n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n-i+1):
        if y == i*10000 + j*5000 + (n-i-j)*1000:
            print(i, j, (n-i-j))
            exit()
print(-1,-1,-1)
