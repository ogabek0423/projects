import random


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    i=0
    while low <= high:
        i=i+1
        mid = (low + high)//2

        if target == arr[mid]:
            return mid,i

        elif target > arr[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return None

l = [100, 1, 2, 5, 7, 9, 0, 3, 4, 6, 7, 12, 15, 98, 65, 23, 27, 99]

tar = 27

l.sort()
print(l)
res = binary_search(l, tar)
print("natija:", res)
