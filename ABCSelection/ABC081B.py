#https://atcoder.jp/contests/abs/tasks/abc081_b

a = int(input())
inputs = list(map(int, input().split()))
sum = 0
while True:
    for i in range(0,a):
        if inputs[i] % 2 :
            #ここでbreakするとelse無視して下のbreakへ
            break
        inputs[i] = inputs[i] / 2
    else:
        sum += 1
        continue
    break
print("%d" %(sum))