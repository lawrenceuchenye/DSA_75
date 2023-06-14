
# binary search function
def binary_search(list, target):
    mid = len(list)//2

    # check if only one element is in the array
    # check if element is target
    # return True if is else False
    if (len(list) == 1):
        if (list[0] == target):
            print("Target Found")
            return True
        return False

    # check if target in the middle
    if (list[mid] == target):
        print("Target Found")
        return True

    # split array in half
    sub_list_l, sub_list_r = list[mid:], list[:mid]

    # store traversal return state
    left = binary_search(sub_list_l, target)
    right = binary_search(sub_list_r, target)

    # if any is true return True esle
    return (left or right) if True else False


# function call
print(binary_search([1, 2, 3, 4, 5, 6], 7))
