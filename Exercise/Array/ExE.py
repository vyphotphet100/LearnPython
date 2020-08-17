def delElemt(arr, x):
    i = 0
    while (i < len(arr)):
        if (arr[i] == x):
            arr.pop(i)
            i -= 1
        else:
            i += 1

arr = [6,4,8,7,3]
delElemt(arr, 7)
print(arr)