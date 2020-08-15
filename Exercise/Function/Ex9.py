def PhanTu(n):
    if (n == 0):
        return a0
    return PhanTu(n-1)*q

a0, q, n = list(map(int, input().split(" ")))

print("Phan tu thu %d la %d" % (n,PhanTu(n)))

s = 0
for i in range(0, n+1):
    s += PhanTu(i)
print("Tong: %d" %s)

