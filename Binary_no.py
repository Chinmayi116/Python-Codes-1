class Search:
    def __init__(self, arr):
        self.arr = arr

    def binary(self, key):
        low = 0
        high = len(self.arr)-1
        while low <= high:
            mid = (low+high)//2
            if self.arr[mid] == key:
                return mid
            elif key < self.arr[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1

s = Search([1,3,5,7,9])
print("Found at:", s.binary(7))
