def quickSort(arr, l, r, mode):
    if (mode == 0):
        return 

    anchor = int((l+r)/2)
    i = l
    j = r
    while (i<j):
        if (mode > 0):
            while (i<anchor and arr[i] <= arr[anchor]):
                i += 1
            while (j>anchor and arr[j] >= arr[anchor]):
                j -= 1
        else:
            while (i<anchor and arr[i] >= arr[anchor]):
                i += 1
            while (j>anchor and arr[j] <= arr[anchor]):
                j -= 1

        if (i<j):
            if (i == anchor):
                anchor = j
            elif (j == anchor):
                anchor = i

            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    if (l<anchor):
        quickSort(arr, l, anchor, mode)
    if (anchor+1 < r):
        quickSort(arr, anchor+1, r, mode)

arr = [1,6,2,8,4,7,2]
quickSort(arr, 0, len(arr)-1, -1)
print(arr)