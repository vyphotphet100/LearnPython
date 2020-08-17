def searchVal(arr, k):
    for i in range(0, len(arr)):
        if (arr[i] == k):
            return i
    return -1

arr = [3,7,5,8,9,2,5,4,7]
print(searchVal(arr, 5))
