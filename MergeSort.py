def merge_sort(arr1, arr2):  # Conditon is Both array should be sorted
    i = j = k = 0
    l1 = len(arr1)
    l2 = len(arr2)
    arr = [0] * (l1 + l2)
    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1

        else:
            arr[k] = arr2[j]
            k = k + 1
            j = j + 1
    while (i < len(arr1)):
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1
    while (j < len(arr2)):
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1
    return arr


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 4, 6, 8, 9]

print(merge_sort(arr1, arr2))
# print(arr)
