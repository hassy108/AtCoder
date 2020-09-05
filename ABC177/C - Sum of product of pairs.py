#https://atcoder.jp/contests/abc177/tasks/abc177_c

"""
N = int(input())
A = [int(x) for x in input().split()]
s = 0
CONST = 10**9+7
for i in range(N-1):
    for j in range(i+1, N):
        s += (A[i] * A[j]) % CONST
print(s%CONST)

"""
"""
上の方法ではO(N^2)で制限時間を超える
累積和を使えばO(1)で終わる
"""
N = int(input())
A = [int(x) for x in input().split()]
S = [0] * (N+1)      #累積和用のリスト
s = 0
CONST = 10**9+7

#前準備として累積和を計算
for i in range(N):
    S[i+1] = S[i] + A[i]

#積の総和を計算
for i in range(N-1):
    s += A[i] * ((S[N] - S[i+1]) % CONST)
    s %= CONST

print(s)
