
def product_except_self(arr):
    nums = [1]*len(arr)

    prefix, postfix = 1, 1
    for x in range(len(nums)):
        nums[x] = prefix
        prefix *= arr[x]

    for x in range(len(nums)-1, -1, -1):
        nums[x] *= postfix
        postfix *= arr[x]

    print(nums)


arr = [1, 2, 3, 4]
product_except_self(arr)
