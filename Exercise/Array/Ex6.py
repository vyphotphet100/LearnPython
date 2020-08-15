def genFiboArr(n):
    arr = [0, 1, 1]
    for i in range(3, n):
        arr.append(arr[i-2] + arr[i-1])
    return arr

def sumArr(fiboArr):
    s = 0
    for i in range(1, len(fiboArr)):
        s += 1/fiboArr[i]
    return s

n = int(input("Input n: "))
fiboArr = genFiboArr(n)
print("The fibonacci array: {}".format(fiboArr))
print("Sum = %f" % sumArr(fiboArr))

fiboArr.reverse()
print("After reversing: {}".format(fiboArr))

