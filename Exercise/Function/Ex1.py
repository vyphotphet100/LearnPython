import math

def isPrime(n):
    if (n<2):
        return False
    elif(n==2):
        return True
    else:
        if (n%2 == 0):
            return False
        else:
            for i in range(3, int(math.sqrt(n))+1, 2):
                if (n%i == 0):
                    return False
    return True

def isSquare(n):
    return (int(math.sqrt(n)) == float(math.sqrt(n)))

def isPerfect(n):
    s = 0
    for i in range(1, n/2+1):
        if (n%i == 0):
            s += i
    return (n == s)
        


while (True):
    n = int(input("Input n: "))
    if (isPerfect(n)):
        print("YES")
    else:
        print("NO")
