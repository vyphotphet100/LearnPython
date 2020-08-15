def inputArr(arr, n):
    for i in range(0, n):
        tmp = int(input("A[%d] = " % i))
        arr.append(tmp)

def outputArr(arr):
    print("The array: {}".format(arr))

def isPalindrome(arr):
    for i in range(0, int(len(arr)/2)):
        if (arr[i] != arr[-1-i]):
            return False
    return True

n = int(input("Input n: "))
arr = []
inputArr(arr, n)
outputArr(arr)
if (isPalindrome(arr)):
    print("This array is palindromic.")
else:
    print("This array is not palindromic.")

