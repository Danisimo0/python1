a = []
n = int(input("n = "))

for _ in range(n):
    a.append(float(input("value = ")))

k = int(input("k = "))
l = int(input("l = "))
summa = 0
for index in range(k - 1, l):
    summa += a[index]

print(summa)
print(sum(a[k-1:l]))
