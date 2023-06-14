
def bubble_sort(arr):
    i, j = None, None
    for y in range(len(arr)-1):
        for x in range(len(arr)-1):
            i, j = arr[x], arr[x+1]
            if i > j:
                arr[x], arr[x+1] = j, i
    print(arr)


bubble_sort([1, 4, 8, 6, 3, 2, 9, 7])
