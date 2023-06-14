
# main class
class CustomArray:
    def __init__(self, main_array):
        self.main_array = main_array

    # function to inser into the array
    def insert(self, target, pos):
        temp = None
        for i in range(len(self.main_array)-1):
            if i > pos:
                temp = self.main_array[i+1]
                self.main_array[i+1] = self.main_array[i]
                self.main_array[i+1] = temp
        self.main_array[pos] = target

    # function to delete from the array
    def delete(self, pos):
        for i in range(len(self.main_array)):
            if i > pos:
                self.main_array[i-1] = self.main_array[i]
        # set empty spaces to -1
        self.main_array[-1] = -1

    # function to get from the array
    def get(self, pos):
        return self.main_array[pos]


arr = CustomArray([1, 2, 3, 4, 5, 6])
arr.insert(256, 3)
print(arr.main_array, "\n")
arr.delete(1)
print(arr.main_array, "\n")
print(arr.get(2))
