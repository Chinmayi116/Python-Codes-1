class Numbers:
    def __init__(self, nums):
        self.nums = nums

    def find(self):
        print("Largest:", max(self.nums))
        print("Smallest:", min(self.nums))

n = Numbers([10, 5, 20, 2])
n.find()
