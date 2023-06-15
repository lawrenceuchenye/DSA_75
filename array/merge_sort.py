
def merge_sort(arr):
    if (len(arr) == 1):
        return arr
    mid = len(arr)//2
    arr_l = arr[mid:]
    arr_r = arr[:mid]
    merge_sort(arr_l)
    merge_sort(arr_r)

    i = j = k = 0

    while i < len(arr_l) and j < len(arr_r):
        if arr_l[i] < arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1
        k += 1
    while i < len(arr_l):
        arr[k] = arr_l[i]
        i += 1
        k += 1

    while j < len(arr_r):
        arr[k] = arr_r[j]
        j += 1
        k += 1

    print(arr)


merge_sort([1, 3, 5, 6, 8, 2, 0])
