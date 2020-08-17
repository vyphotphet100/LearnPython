def searchValArr(arr, k):
    ans = []
    for i in range(0, len(arr)):
        if (arr[i] == k):
            ans.append(i)
    return ans

arr = [3,7,6,5,8,2,5,4]
print(searchValArr(arr, 7))
