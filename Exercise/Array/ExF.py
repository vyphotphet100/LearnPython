def delCommon(arr):
    i = 0
    while (i<len(arr)-1):
        checkComm = False
        j = i+1
        while (j<len(arr)):
            if (arr[j] == arr[i]):
                arr.pop(j)
                checkComm = True
                j -= 1
            j += 1
        if (checkComm):
            arr.pop(i)
            i -= 1
        i += 1

arr = [6,4,8,7,3,2,7,4]
delCommon(arr)
print(arr)