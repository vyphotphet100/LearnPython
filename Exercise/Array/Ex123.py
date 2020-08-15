def inputArr(arr):
    global n
    n = int(input("Input n: "))
    for i in range(0, n):
        tmp = int(input("a[%d] = " %i))
        arr.append(tmp)

def outputArr(arr):
    print("The array: ", end = "")
    for i in range(0, n):
        print(arr[i], end = " ")
    print()

def printEven(arr):
    print("The even values: ", end = "")
    for i in range(0, n):
        if (arr[i]%2 == 0):
            print (arr[i], end = " ")
    print()

def printOdd(arr):
    print("The odd values: ", end = "")
    for i in range(0, n):
        if (arr[i]%2):
            print(arr[i], end = " ")
    print()

def printEvenIndex(arr):
    print("Even value indexes: ", end = "")
    for i in range(0, n):
        if (arr[i]%2 == 0):
            print(i, end = " ")
    print()

def turnToOdd(arr):
    for i in range(0, n):
        if (arr[i]%2 == 0):
            arr[i] += 1

def smallestVal(arr):
    ans = arr[0]
    for i in range(0, n):
        if (arr[i] < ans):
            ans = arr[i]
    return ans

def highestVal(arr):
    ans = arr[0]
    for i in range(0, n):
        if (arr[i] > ans):
            ans = arr[i]
    return ans

def avgVal(arr):
    s = 0
    for i in range(0, n):
        s += arr[i]
    return s/n

def binarySearch(arr, start, end, k):
    arr.sort()
    ptint("After sorting: ")
    outputArr(arr)

    while (start <= end):
        mid = int((start + end)/2)
        if (arr[mid] < k):
            start = mid + 1
        elif (arr[mid] > k):
            end = mid - 1
        else:
            return mid
    return -1

def findVal(arr, k):
    for i in range(0, n):
        if (arr[i] == k):
            return i
    return -1


n = 0
arr = []
inputArr(arr)
outputArr(arr)
# printEven(arr)
# printOdd(arr)
# printEvenIndex(arr)

# print("After turning into Odd: ")
# turnToOdd(arr)
# outputArr(arr)

# print("The smallest value of the array: %d" % smallestVal(arr))
# print("The highest value of the the array: %d" % highestVal(arr))
# print("The average value of elements of the array: %f" % avgVal(arr))

k = int(input("Input k: "))
#print("After searching: %d" % binarySearch(arr, 0, n-1, k))
print("After searching: %d" % findVal(arr, k))


