def searchVal(arr, k):
    for i in arr:
        if (i == k):
            return True
    return False

arr = []
i = 1
while (i <= 20): 
    n = int(input("Input the element %d: " % i))
    if (n < 10 or n > 100):
        print("Inputted number is invalid.")
        continue
    if (searchVal(arr, n)):
        print("Inputted value has appeared.")
        continue

    arr.append(n)
    i += 1

print("The value of the array: ")
print(arr)

