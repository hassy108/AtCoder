#https://atcoder.jp/contests/abs/tasks/abc081_a

i = int(input())
sum = 0;
while i > 0:
    sum += i%10
    i /= 10
else:
    print("%d" %(sum))
