
n = int(input())
l = [int(x) for x in input().split()]
c = 0
for i in range(n):
    for j in range(i+1,n):
        if l[i] == l[j]:
            continue
        for k in range(j+1,n):
            if l[i] == l[k] or l[j] == l[k]:
                continue
            if l[i]+l[j] > l[k] and l[i]+l[k] > l[j] and l[j]+l[k] > l[i]:
                c += 1
print(c)