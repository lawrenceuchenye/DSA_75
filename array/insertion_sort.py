
def insertion_sort(arr):
    # for loop thoru array from 1
    for x in range(1, len(arr)):
        # store indx val
        # store predecesdor indx
        temp = arr[x]
        j = x-1
        # constraints
        # if j >= 0
        # temp isboess than current j indx
        while ((j >= 0) and (temp < arr[j])):
            # push current j_val to the back
            # decrease j
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    print(arr)


insertion_sort([1, 7, 3, 4, 9, 10, 1, 2, 5])
