def PhanTu(n):
    if (n == 0):
        return a0
    return (PhanTu(n-1) + d)

a0 = int(input())
d = int(input())
n = int(input())
print(PhanTu(n))
