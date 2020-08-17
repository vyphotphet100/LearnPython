def quickSort(arr, l, r):
    anchor = int((l+r)/2)

    i = l
    j = r
    while (i<j):
        while (i < anchor and arr[i] <= arr[anchor]):
            i += 1
        while (j > anchor and arr[j] >= arr[anchor]):
            j -= 1
        
        if (i < j):
            if (i == anchor):
                anchor = j
            elif(j == anchor):
                anchor = i

            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    if (l < anchor):
        quickSort(arr, l, anchor)
    if (anchor+1 < r):
        quickSort(arr, anchor+1, r)

arr = [1,7,4,5,6,5,8,2]
quickSort(arr, 0, len(arr)-1)
print(arr)

         