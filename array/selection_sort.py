

def selection_sort(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[y] > arr[x]:
                temp = arr[y]
                arr[y] = arr[x]
                arr[x] = temp
    print(arr)


selection_sort([1, 4, 2, 7, 8, 3, 0, 5])
