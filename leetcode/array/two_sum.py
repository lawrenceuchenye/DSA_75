
def twoSum(num_arr, target):
    prevMap = {}  # val:indx

    # loop through index,val
    for i, n in enumerate(num_arr):
        # fimd diff [missing piece]
        diff = target-n

        # ilif diff existed return
        if diff in prevMap:
            return [prevMap[diff], i]
        # update prevMap if piece not found
        prevMap[n] = i


# print/call function
print(twoSum([2, 5, 4, 7, 8], 13))
