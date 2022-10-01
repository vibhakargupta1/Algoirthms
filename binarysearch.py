def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
 
arr = []
len = int(input("Enter length of array"))
for i in range(len):
    temp = int(input())
    arr.append(temp)
x = int(input("Enter number to be searched for"))
result = binary_search(arr, 0, len-1, x)
 
if result != -1:
    print("Element found at :", str(result))
else:
    print("Element not found")