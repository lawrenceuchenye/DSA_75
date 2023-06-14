
def maxSub(arr):
    maxSub = arr[0]
    currSum = 0
    for n in range(len(arr)):
        if currSum < 0:
            currSum = 0
        currSum += arr[n]
        maxSub = max(maxSub, currSum)
    return maxSub


print(maxSub([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
