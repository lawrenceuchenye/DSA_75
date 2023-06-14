
#O(n) algoruthm test
def linear_search(list,target):
    """
      Return index of target else return none
    """
    for indx in range(0,len(list)):
        if list[indx]==target:
            return indx
    return None

def verify(indx):
    if indx is not None:
        print("Target Found At Index:[{}]".format(indx))
    else:
        print("Index not found in list")


numbers=[1,2,3,4,5,6,7,8,9,10]

result=linear_search(numbers,6)
verify(result)



