def printF(arr):
    for i in range(len(arr)):
        print(*arr)
    return 0


a = [1, 1.0, "A", 'a', True]
a.pop(1)
a.clear()
a += [i for i in range(100)]
b = [10, 20, 30, 40]
s = a + b
a.extend(b)
b.append("QQQQQQQ")
a.append(10)
z = [[1, 2, 3, 4, 5]]
for i in range(1, 5):
    tmp = [i]
    for j in range(1, 5):
        print(tmp, z)
        tmp += [i * z[0][j]]
    z.append(tmp)
printF(z)
