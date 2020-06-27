import numpy as np
a = list(np.random.rand(13,))
def merge_sort(arr):
    lentgh = len(arr)
    left_len = lentgh // 2
    left = arr[:left_len]
    right = arr[left_len:]
    if left_len == 1 and len(right) == 1:
        pass
    elif left_len == 1:
        right = merge_sort(right)
    else:
        left = merge_sort(left)
        right = merge_sort(right)
    i = 0
    j = 0
    result = []
    for _ in range(len(arr)-1):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1 
        if i > len(left)-1: return  result + right[j:]
        elif j > len((right))-1: return result + left[i:]      
    return result
print(merge_sort(a))


