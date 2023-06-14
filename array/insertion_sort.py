
def insertion_sort(arr):
    i, j, temp = None, None, None
    ival, jval = None, None
    for x in range(len(arr)-1):
        i, j, ival, jval = x, x+1, arr[x], arr[x+1]
        temp = arr[x]
        while ((jval < temp) and (j >= 0)):
            arr[j+1] = arr[j]
            j -= 1
            jval = arr[j]
        arr[j+1] = temp
    print(arr)


insertion_sort([1, 7, 3, 4, 9, 10, 1, 2, 5])
