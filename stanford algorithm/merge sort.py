import numpy as np
arr = [1,5,3,90,100,33,76,11]
def merge_sort(arr):
    length = len(arr)
    left_half = length // 2
    right_half = length - left_half
    left = arr[ : left_half]
    right = arr[left_half :]
    result = []
    if left_half == 1 and right_half == 1:
        pass
    elif left_half == 1:
        right = merge_sort(right)
    else:
        left = merge_sort(left)
        right = merge_sort(right)
    result = []
    i= 0
    j= 0
    for _ in range(len(arr)):
        if left[i] < right [j]:
            result.append(left[i])
            i += 1
            if i > len(left)-1: return result + right[j:]
        else:
            result.append(right[j])
            j += 1
            if j > len(right)-1: return result + left[i:]
print(merge_sort(arr))  
