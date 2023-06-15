
def merge_sort(arr):
    # terminate recursion if only 1 element in array
    if (len(arr) == 1):
        return arr

    # split array into two
    mid = len(arr)//2
    arr_l = arr[mid:]
    arr_r = arr[:mid]

    # sort left/right array
    merge_sort(arr_l)
    merge_sort(arr_r)

    i = j = k = 0

    # merge by looping till one array is completely merged
    while i < len(arr_l) and j < len(arr_r):
        if arr_l[i] < arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1
        k += 1

    # check for unfinished artay to.merge
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
