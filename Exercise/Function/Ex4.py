def s(n):
    if (n == 1):
        return 1
    return n + s(n-1)

while (True):
    n = int(input("Input n: "))
    if (n>0): break

print("Sum: %d" %s(n))
