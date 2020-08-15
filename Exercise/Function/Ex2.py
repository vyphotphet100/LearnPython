def gcd(a, b):
    if (a < b):
        tmp = a
        a = b
        b = tmp
    
    if (a%b == 0):
        return b
    else:
        return gcd(b, a%b)

def lcd(a, b):
    return (a*b)/gcd(a,b)

def gArrVal(arr):
    ans = arr[0]
    for i in arr:
        if (i > ans):
            ans = i
    return ans

def sArrVal(arr):
    ans = arr[0]
    for i in arr:
        if (i < ans):
            ans = i
    return ans

def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def C(k, n):
    factN = fact(n)
    factK = fact(k)
    factNK = fact(n-k)

    return int(factN/(factK*factNK))

def A(k, n):
    factN = fact(n)
    factNK = fact(n-k)

    return int(factN/factNK)

n = int(input())
k = int(input())
print(A(k, n))

