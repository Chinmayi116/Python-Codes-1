class Calculator:
    def add(self, *numbers):
        total = 0
        for n in numbers:
            total += n
        return total

obj = Calculator()

print(obj.add(10))
print(obj.add(10, 20))
print(obj.add(10, 20, 30, 40))
