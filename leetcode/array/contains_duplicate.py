
def contains_duplicate(arr):
    hashset = set()
    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(contains_duplicate([1, 2, 3, 4, 1]))
