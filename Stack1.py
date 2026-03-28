# Stack implementation with user input

stack = []

n = int(input("Enter number of elements: "))

# Taking elements from user (Push)
for i in range(n):
    element = int(input("Enter element: "))
    stack.append(element)

print("Stack after push:", stack)

# Pop operation
if len(stack) == 0:
    print("Stack is empty")
else:
    removed = stack.pop()
    print("Popped element:", removed)

# Peek operation
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Top element:", stack[-1])

# Display final stack
print("Final Stack:", stack)
