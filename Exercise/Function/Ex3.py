def convertCountingSystem(n, k):
    if (k<2 or k>16 or n<0):
        return None
    
    ans = ""
    while (n!=0):
        if (n%k < 10):
            ans = str(n%k) + ans
        elif (n%k == 10):
            ans = "A" + ans
        elif (n%k == 11):
            ans = "B" + ans
        elif (n%k == 12):
            ans = "C" + ans
        elif (n%k == 13):
            ans = "D" + ans
        elif (n%k == 14):
            ans = "E" + ans
        else:
            ans = "F" + ans
            
        n = int(n/k)
    
    return ans

n = k = -1
while (n < 0 or k<2 or k>16):
    n = int(input("Input n: "))
    k = int(input("Input k: "))

print("After converting: %s" % convertCountingSystem(n, k))