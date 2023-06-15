

def partiton(arr, start, end):
    pivot = arr[end]
    i = start-1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i += 1
    temp = arr[i]
    arr[i] = arr[end]
    arr[end] = temp

    return i


def quick_sort(arr, start, end):
    if end <= start:
        return
    pivot = partiton(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

    return arr


print(quick_sort([1, 6, 7, 3, 2, 0, 8, 5], 0, 8-1))
