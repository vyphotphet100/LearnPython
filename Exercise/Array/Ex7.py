def selectionSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] > arr[j]):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

arr = [2,8,3,9,8,7,3,7]
selectionSort(arr)
print(arr)
